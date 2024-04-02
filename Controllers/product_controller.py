from db import init_db, db
from flask import Flask, jsonify
from util.reflection import populate_object
from models.categories import Categories
from models.products import Products, product_schema

def product_add(req):
    post_data = req.form if req.form else req.json
    new_product = Categories.get_new_product()

    populate_object(new_product, post_data)
    db.session.add(new_product)
    db.commit(new_product)


def products_get_all():
    products_query = db.session.query(Products).all()

    return jsonify({"message": "products found", "results": product_schema.dump(products_query)}), 200


def get_product_by_id(req, product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id)


    if product:
        return jsonify({"message": "product found", "results": product_schema.dump(product)}), 200
    else:
        return jsonify("you messed up a-aron"), 400


def product_activity(req: Request, product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id)

    if product:
        product.active = True

        db.session.add(product)
        db.commit(product)


        return jsonify({"message": "product has been activated"}), 200
            
    else:

        return jsonify({"product with product_id: {product_id} not found"}), 404


def product_update(req,  product_id):
    post_data = req.form if req.form else req.json
    product = db.session.query(Products).filter(Products.product_id == product_id)

    if product:
        product_record = {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "description": product.description,
            "price": product.price,
            "active": product.active
        }

        for key in product_record.keys():

            try:
                product_record[key] = post_data[key]

            except:
                pass

        
        populate_object(product, post_data)
        db.session.add(product)
        db.commit(product)

        return jsonify({"message": "product updated", "results": product_schema.dump(product)}), 200
   

    return jsonify(f"product with ID {product_id} could not be found")


def product_delete_by_id(req, product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id)
    if product:
        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": "product deleted"}), 200

    return jsonify({"message": "product not found"}), 404