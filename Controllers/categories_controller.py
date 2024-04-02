from db import init_db, db
from flask import Flask, jsonify
from util.reflection import populate_object
from models.categories import Categories, category_schema
import marshmallow as ma

def category_add(req):
    post_data = req.form if req.form else req.json
    new_category = Categories.get_new_category()

    populate_object(new_category, post_data)
    db.session.add(new_category)
    db.commit(new_category)


def category_get_all():
    category_query = db.session.query(Categories).all()

    return jsonify({"message": "category found", "results": category_schema.dump(category_query)}), 200


def get_category_by_id(req, category_id):
    category = db.session.query(Categories).filter(Categories.category_id == category_id)


    if category:
        return jsonify({"message": "category found", "results": category_schema.dump(category)}), 200
    else:
        return jsonify("you messed up a-aron"), 400


def category_activity(req, category_id):
    category = db.session.query(Categories).filter(Categories.category_id == category_id)

    if category:
        category.active = True

        db.session.add(category)
        db.commit(category)


        return jsonify({"message": "category has been activated"}), 200
            
    else:

        return jsonify({"category with product_id: {product_id} not found"}), 404


def category_update(req,  category_id):
    post_data = req.form if req.form else req.json
    category = db.session.query(Categories).filter(Categories.category_id == category_id)

    if category:
        category_record = {
            "category_id": category.category_id,
            "category_name": category.category_name,
            "active": category.active
        }

        for key in category_record.keys():

            try:
                category_record[key] = post_data[key]

            except:
                pass

        
        populate_object(category, post_data)
        db.session.add(category)
        db.commit(category)

        return jsonify({"message": "category updated", "results": category_schema.dump(category)}), 200
   

    return jsonify(f"category with ID {category_id} could not be found")


def category_delete_by_id(req, category_id):
    category = db.session.query(Categories).filter(Categories.category_id == category_id)
    if category:
        db.session.delete(category)
        db.session.commit()

        return jsonify({"message": "category deleted"}), 200

    return jsonify({"message": "category not found"}), 404