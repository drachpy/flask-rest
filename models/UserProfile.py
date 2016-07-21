from schema import Schema, And, Use, Optional
from . import Crud, db


class UserProfile(db.Model, Crud):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)


class UserProfileValidator():
    def validate(self, req):
        schema = Schema(
            {
                'username': And(str, len, error='Username is required'),
                'password': And(str, len, error='Password is required'),
                'email': And(str, len, error='Email is required'),
                # Optional('gender'): And(
                #         str,
                #         Use(str.lower),
                #         lambda s: s in ('male', 'female')
                #     ),
                # 'age':  And(Use(int), lambda n: 18 <= n <= 99)
            }
        )

        return schema.validate(req)
