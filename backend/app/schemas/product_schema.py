from marshmallow import Schema, fields, validate

# Schema for Products collection
class ProductSchema(Schema):
    _id = fields.Str(required=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    image_url = fields.Url()
