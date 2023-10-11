import unittest

from werkzeug.exceptions import InternalServerError

from app import create_app
from app.models.customer_model import CustomerModel
from app.models.product_model import ProductCustomerModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_get_by_id_single(self):
        model = CustomerModel()
        with self.app.app_context():
            result = model.get_by_id("1", "12345678")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, CustomerModel)

    def test_get_by_id_single_invalid(self):
        model = CustomerModel()
        with self.app.app_context():
            result = model.get_by_id("5", "12345678")
        self.assertIsNone(result)

    def test_get_by_id_single_server_error(self):
        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:PpvBmpxmmkHlvPs@containers-us-west-91.railway.app:7825/railway"
        model = CustomerModel()
        with self.assertRaises(InternalServerError):
            result = model.get_by_id("5", "12345678")

    def test_get_by_id_multiple(self):
        model = ProductCustomerModel()
        with self.app.app_context():
            result = model.get_by_id(2, 12345679, many=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        if result:
            self.assertIsInstance(result[0], ProductCustomerModel)

    def test_get_by_id_multiple_invalid(self):
        model = ProductCustomerModel()
        with self.app.app_context():
            result = model.get_by_id(5, 12345679, many=True)
        self.assertIsNone(result)
