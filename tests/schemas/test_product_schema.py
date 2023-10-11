import json
import unittest

from marshmallow import ValidationError

from app.schemas.product_schema import ProductDataSchema


class TestCustomerSchema(unittest.TestCase):
    def setUp(self):
        self.schema = ProductDataSchema()
        with open("./tests/product_data.json", "r") as file:
            self.json_data = json.load(file)

    def test_valid_data(self):
        result = self.schema.load(self.json_data)
        self.assertTrue(result, dict)
        if isinstance(result, dict):
            self.assertIn("type_id", result)
            self.assertIn("identification", result)
            self.assertIn("cut_off_date", result)
            self.assertIn("product_id", result)

    def test_invalid_serialization(self):
        self.json_data.pop("type_id")
        with self.assertRaises(ValidationError):
            self.schema.load(self.json_data)

    def test_invalid_data_type(self):
        self.json_data["product_id"] = 34
        try:
            self.schema.load(self.json_data)
        except ValidationError as e:
            self.assertIn("product_id", e.messages)
            self.assertEqual(e.messages["product_id"][0], "Not a valid string.")
