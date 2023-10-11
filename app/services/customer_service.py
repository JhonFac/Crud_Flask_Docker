from app.models.customer_model import CustomerModel


class CustomerService:
    def __init__(self):
        self.customerModel = CustomerModel()

    def get_by_id(self, typeId, customId):
        return self.customerModel.get_by_id(typeId, customId)
