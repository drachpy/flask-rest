from flask import request, jsonify, make_response
from flask_restful import Resource
from functional import seq

from models.Book import Book, BookValidator


class BookList(Resource):
    def get(self):
        query = Book.query.all()

        resp = make_response(jsonify(
            seq(query)\
            .select(lambda p:
            {
                'id': p.id,
                'code': p.code
            })\
            .to_list()
        ))
        resp.status_code = 200
        return resp

    def post(self):
        try:
            req = request.get_json(force=True)
            data = BookValidator().validate(req)

            resource = Book()
            query = resource.add(data)
            return BookDetail().get(query.id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 403
            return resp


class BookDetail(Resource):
    def get(self, id):
        query = Book.query.get_or_404(id)

        resp = make_response(jsonify(
            seq([query])\
            .select(lambda p:
            {
                'id': p.id,
                'code': p.code
            })\
            .first()
        ))
        resp.status_code = 200
        return resp

    def put(self, id):
        try:
            req = request.get_json(force=True)
            data = BookValidator().validate(req)

            resource = Book.query.get_or_404(id)
            resource.update(data)

            return self.get(id)

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        try:
            resource = Book.query.get_or_404(id)
            resource.delete()
            resp = make_response()
            resp.status_code = 204
            return resp

        except Exception as ex:
            resp = jsonify({"error": str(ex)})
            resp.status_code = 401
            return resp

