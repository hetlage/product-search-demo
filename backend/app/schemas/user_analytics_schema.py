from marshmallow import Schema, fields, validate


# Schema for User Analytics collection
class UserAnalyticsSchema(Schema):
    _id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    search_term = fields.Str(required=True)
    search_location = fields.Dict(
        required=True,
        keys=fields.Str(validate=validate.OneOf(["latitude", "longitude"])),
        values=fields.Float(),
    )
    timestamp = fields.DateTime(required=True)
