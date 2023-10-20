from app.models.customer_model import CustomerModel


class CustomerService:
    def __init__(self):
        self.customer_model = CustomerModel()

    def get_by_id(self, type_id, custom_id):
        return self.customer_model.get_by_id(type_id, custom_id)
