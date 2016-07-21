from flask import request, jsonify, make_response
from flask_restful import Resource
from functional import seq

from models.UserProfile import UserProfile, UserProfileValidator


class UserProfileList(Resource):
    def get(self):
        query = UserProfile.query.all()

        resp = make_response(jsonify(
            seq(query)\
            .select(lambda p:
            {
                'id': p.id,
                'username': p.username,
                'password': p.password,
                'email': p.email
            })\
            .to_list()
        ))
        resp.status_code = 200
        return resp

    def post(self):
        try:
            req = request.get_json(force=True)
            data = UserProfileValidator().validate(req)

            # Sample adding explicitly
            # resource = UserProfile(
            #     username=data['username'],
            #     password=data['password'],
            #     email=data['email']
            # )
            # resource.add()

            resource = UserProfile()
            query = resource.add(data)
            return UserProfileDetail().get(query.id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 403
            return resp


class UserProfileDetail(Resource):
    def get(self, id):
        query = UserProfile.query.get_or_404(id)

        resp = make_response(jsonify(
            seq([query])\
            .select(lambda p:
            {
                'id': p.id,
                'username': p.username,
                'password': p.password,
                'email': p.email
            })\
            .first()
        ))
        resp.status_code = 200
        return resp

    def put(self, id):
        try:
            req = request.get_json(force=True)
            data = UserProfileValidator().validate(req)

            resource = UserProfile.query.get_or_404(id)
            # Sample update explicitly
            # for key, value in data.items():
            #     setattr(resource, key, value)
            # resource.update()
            resource.update(data)

            return self.get(id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        try:
            resource = UserProfile.query.get_or_404(id)
            resource.delete()
            resp = make_response()
            resp.status_code = 204
            return resp

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp
