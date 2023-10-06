from flask import request
from flask_restful import Resource

from app.schemas.client_schema import ClientSchema
from app.services.service import Service
from app.utils.response import error_response, success_response


class Controller(Resource):
    def __init__(self):
        self.service = Service()
        self.schema = ClientSchema()

    def get(self, typeId=None, customId=None):
        response = self.service.get_by_id(typeId, customId)
        if response:
            return success_response(self.schema.dump(response))
        else:
            return error_response("No Content", 204)

    def post(self, data=None):
        errors = self.schema.validate(data)
        if errors:
            return error_response(errors, 400)
        response = self.example_service.create(data)
        return success_response(response)
        # return success_response(self.example_schema.dump(example), 201)

    def put(self, id):
        data = request.get_json()
        errors = self.example_schema.validate(data)
        if errors:
            return error_response(errors, 400)
        example = self.example_service.update_example(id, data)
        if example:
            return success_response(self.example_schema.dump(example))
        else:
            return error_response("Example not found", 404)

    def delete(self, data):
        errors = self.schema.validate(data)
        if errors:
            return error_response(errors, 400)
        if self.example_service.delete_example(data["tipo_id"]):
            return success_response("Successfully removed")
        return error_response("Delete not found", 404)
