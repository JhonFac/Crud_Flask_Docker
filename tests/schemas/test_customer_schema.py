import json
import unittest

from marshmallow import ValidationError

from app.schemas.client_schema import ClientSchema


class TestCustomerSchema(unittest.TestCase):
    def setUp(self):
        self.schema = ClientSchema()
        with open("./tests/customer_data.json", "r") as file:
            self.json_data = json.load(file)

    def test_valid_data(self):
        result = self.schema.load(self.json_data)
        self.assertTrue(result, dict)
        if isinstance(result, dict):
            self.assertIn("type_id", result)
            self.assertIn("identification", result)
            self.assertIn("name", result)

    def test_invalid_serialization(self):
        self.json_data.pop("type_id")
        with self.assertRaises(ValidationError):
            self.schema.load(self.json_data)

    def test_invalid_data_type(self):
        self.json_data["client_segment"] = 34
        try:
            self.schema.load(self.json_data)
        except ValidationError as e:
            self.assertIn("client_segment", e.messages)
            self.assertEqual(e.messages["client_segment"][0], "Unknown field.")
