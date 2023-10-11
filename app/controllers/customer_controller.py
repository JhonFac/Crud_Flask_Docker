from flask_restful import Resource

from app.services.customer_service import CustomerService


class CustomerController(Resource):
    def __init__(self):
        self.customer_service = CustomerService()

    def get_client(self, typeId: int = None, customId: int = None):
        if typeId != None and customId != None:
            return self.customer_service.get_by_id(typeId, customId)
        return None
