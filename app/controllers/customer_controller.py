from flask_restful import Resource

from app.services.customer_service import CustomerService


class CustomerController(Resource):
    def __init__(self):
        self.customer_service = CustomerService()

    def get_client(self, type_id: int = None, custom_id: int = None):
        if type_id != None and custom_id != None:
            return self.customer_service.get_by_id(type_id, custom_id)
        return None
