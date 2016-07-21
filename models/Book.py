from schema import Schema, And, Use, Optional
from . import Crud, db


class Book(db.Model, Crud):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))

class BookValidator():
    def validate(self, req):
        schema = Schema(
            {
                'code': And(str, len, error='Code is required')
            }
        )

        return schema.validate(req)
