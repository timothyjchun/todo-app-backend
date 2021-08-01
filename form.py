from marshmallow import Schema, fields

class TodoSchema(Schema):
    id = fields.Integer(data_key = "id")
    context = fields.String(required = True, data_key = "text")
    color_option = fields.String(required = True, data_key = "color")