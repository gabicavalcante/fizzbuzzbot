from marshmallow import Schema, fields


class ChatAPISchema(Schema):
    id = fields.Str(required=True)
    user = fields.Str(required=True)
    message = fields.Str(required=True)
    response = fields.Str(required=True)
    created_at = fields.DateTime()
