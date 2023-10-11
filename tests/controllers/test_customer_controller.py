import unittest
from unittest.mock import MagicMock

from app.controllers.customer_controller import CustomerController
from app.models.customer_model import CustomerModel


class CustomerControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = CustomerController()
        self.customer_service = MagicMock()
        self.controller.customer_service = self.customer_service

    def test_get_customer_with_invalid_parameters(self):
        result = self.controller.get_client(None, 42)
        assert result == None

    def test_get_customer_with_valid_parameters(self):
        expected_result = CustomerModel()
        self.customer_service.get_by_id.return_value = expected_result
        result = self.controller.get_client(1, 12345678)
        self.assertEqual(result, expected_result)
