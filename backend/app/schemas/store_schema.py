from marshmallow import Schema, fields, validate


# Schema for Stores collection
class StoreSchema(Schema):
    _id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Dict(
        required=True,
        keys=fields.Str(validate=validate.OneOf(["latitude", "longitude"])),
        values=fields.Float(),
    )
    address = fields.Str(required=True)
    phone = fields.Str(validate=validate.Length(min=10, max=15))
