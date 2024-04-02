import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma



from db import db 

class Products(db.Model):
    __tablename__ = "Products"

    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    product_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=True)
    price = db.Column(db.Float(), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, product_name, description, price,  active):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.active = active

    def get_new_product():
        return Products("", "", 0, True)
    

class ProductSchema(ma.Schema):
    class Meta:
            fields = ['product_name', 'description', 'price', 'active']



product_schema = ProductSchema()
products_schema = ProductSchema(many=True)