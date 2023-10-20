import json
import unittest
from unittest.mock import Mock, patch

from werkzeug.exceptions import InternalServerError

from app import create_app
from app.models.customer_model import CustomerModel
from app.models.product_model import ProductCustomerModel
from app.schemas.client_schema import ClientSchema


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.mock_db = Mock()
        self.model = CustomerModel()
        with open("./tests/customer_data.json", "r") as file:
            self.json_data = json.load(file)
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

    @patch("app.models.base_model.BaseModel.get_by_id")
    def test_get_by_id_single(self, mock_get_by_id):
        mock_get_by_id.return_value = CustomerModel(**self.json_data)
        result = self.model.get_by_id(1, 12345678, many=False)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, CustomerModel)
        self.assertIsInstance(result.bank_installments_sum, float)
        self.assertIsInstance(result.capital_balance, float)
        self.assertEqual(result.capital_balance, 10000.5)

    @patch("app.models.base_model.BaseModel.get_by_id")
    def test_get_by_id_single_invalid(self, mock_get_by_id):
        mock_get_by_id.return_value = None
        result = self.model.get_by_id(5, 12345678, many=False)
        self.assertIsNone(result)

    def test_get_by_id_single_server_error(self):
        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:PpvBmpxmmkHlvPs@containers-us-west-91.railway.app:7825/railway"
        model = CustomerModel()
        with self.assertRaises(InternalServerError):
            model.get_by_id(5, 12345678, many=False)

    @patch("app.models.base_model.BaseModel.get_by_id")
    def test_get_by_id_multiple(self, mock_get_by_id):
        model = ProductCustomerModel()
        customer_instances = [
            CustomerModel(**self.json_data),
            CustomerModel(**self.json_data),
            CustomerModel(**self.json_data),
        ]
        mock_get_by_id.return_value = customer_instances
        result = model.get_by_id(1, 12345678, many=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        for customer in result:
            self.assertIsInstance(customer, CustomerModel)

    @patch("app.models.base_model.BaseModel.get_by_id")
    def test_get_by_id_multiple_invalid(self, mock_get_by_id):
        mock_get_by_id.return_value = None
        result = self.model.get_by_id(5, 12345678, many=True)
        self.assertIsNone(result)
