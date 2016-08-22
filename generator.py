"""
Usage:

$ python generator.py Sample

This will create the following files:
1. models/Sample.py
2. resources/Sample.py

And will also add a line in models/models.py
1. from . import Sample

You will need to manually create the endpoints/route in app.py.

"""

import sys


entity_name = sys.argv[1].title()

model = """\
from schema import Schema, And, Use, Optional
from . import Crud, db


class <EntityName>(db.Model, Crud):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))

class <EntityName>Validator():
    def validate(self, req):
        schema = Schema(
            {
                'code': And(str, len, error='Code is required')
            }
        )

        return schema.validate(req)
"""

resource = """\
from flask import request, jsonify, make_response
from flask_restful import Resource
from functional import seq

from models.<EntityName> import <EntityName>, <EntityName>Validator


class <EntityName>List(Resource):
    def get(self):
        query = <EntityName>.query.all()

        resp = make_response(jsonify(
            (seq(query)
            .select(lambda p:
            {
                'id': p.id,
                'code': p.code
            }))
            .to_list()
        ))
        resp.status_code = 200
        return resp

    def post(self):
        try:
            req = request.get_json(force=True)
            data = <EntityName>Validator().validate(req)

            resource = <EntityName>()
            query = resource.add(data)
            return <EntityName>Detail().get(query.id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 403
            return resp


class <EntityName>Detail(Resource):
    def get(self, id):
        query = <EntityName>.query.get_or_404(id)

        resp = make_response(jsonify(
            (seq([query])
            .select(lambda p:
            {
                'id': p.id,
                'code': p.code
            }))
            .first()
        ))
        resp.status_code = 200
        return resp

    def put(self, id):
        try:
            req = request.get_json(force=True)
            data = <EntityName>Validator().validate(req)

            resource = <EntityName>.query.get_or_404(id)
            resource.update(data)

            return self.get(id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        try:
            resource = <EntityName>.query.get_or_404(id)
            resource.delete()
            resp = make_response()
            resp.status_code = 204
            return resp

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp

"""

with open('models/' + entity_name + '.py', 'w') as model_file:
    model_file.write(model.replace("<EntityName>", entity_name))

with open('models/models.py', 'a') as resource_file:
    resource_file.write('from . import ' + entity_name + '\n')

with open('resources/' + entity_name + '.py', 'w') as resource_file:
    resource_file.write(resource.replace("<EntityName>", entity_name))

with open('resources/routes.py', 'a') as writer:
    writer.write('\n')
    writer.write('from resources.{0} import {0}List, {0}Detail\n'\
        .format(entity_name))
    writer.write('api.add_resource({0}List, \'/service/api/{1}\')\n'\
        .format(entity_name, entity_name.lower()))
    writer.write('api.add_resource({0}Detail, \'/service/api/{1}/<id>\')\n'\
        .format(entity_name, entity_name.lower()))

whats_next = """
Step 1: Perform `$ python migrate.py db migrate || python migrate.py db upgrade`
Step 2: Add route to the new resource in `app.py`

"""
print("New model and resource have been generated `" + entity_name + "` .")
print(whats_next)
