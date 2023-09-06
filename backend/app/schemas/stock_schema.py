from marshmallow import Schema, fields, validate


# Schema for Stock collection
class StockSchema(Schema):
    _id = fields.Str(required=True)
    product_id = fields.Str(required=True)
    stores = fields.List(
        fields.Nested(
            {
                "store_id": fields.Str(required=True),
                "stock_level": fields.Int(required=True),
                "last_restocked": fields.DateTime(),
            }
        )
    )
