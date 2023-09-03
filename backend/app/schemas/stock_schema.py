from marshmallow import Schema, fields, validate

# Schema for Stock collection
class StockSchema(Schema):
    _id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    store_id = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=0))
    last_updated = fields.DateTime(required=True)

