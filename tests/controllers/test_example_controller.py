import unittest
from unittest.mock import MagicMock

from app.controllers.controller import Controller


class TestExampleController(unittest.TestCase):
    def setUp(self):
        self.controller = ExampleController()

    def test_get_all_examples(self):
        self.controller.example_service.get_all_examples = MagicMock(return_value=[{"id": 1, "name": "example"}])
        response = self.controller.get()
        self.assertEqual(response[1], 200)
        self.assertEqual(response[0]["data"][0]["id"], 1)
        self.assertEqual(response[0]["data"][0]["name"], "example")

    def test_get_example_by_id(self):
        self.controller.example_service.get_example_by_id = MagicMock(return_value={"id": 1, "name": "example"})
        response = self.controller.get(id=1)
        self.assertEqual(response[1], 200)
        self.assertEqual(response[0]["data"]["id"], 1)
        self.assertEqual(response[0]["data"]["name"], "example")

    def test_get_example_by_id_not_found(self):
        self.controller.example_service.get_example_by_id = MagicMock(return_value=None)
        response = self.controller.get(id=1)
        self.assertEqual(response[1], 404)
        self.assertEqual(response[0]["error"], "not found")

    def test_create_example(self):
        self.controller.example_service.create_example = MagicMock(return_value={"id": 1, "name": "example"})
        response = self.controller.post()
        self.assertEqual(response[1], 201)
        self.assertEqual(response[0]["data"]["id"], 1)
        self.assertEqual(response[0]["data"]["name"], "example")

    def test_create_example_with_validation_errors(self):
        self.controller.example_schema.validate = MagicMock(
            return_value={"name": ["Missing data for required field."]}
        )
        response = self.controller.post()
        self.assertEqual(response[1], 400)
        self.assertEqual(response[0]["error"], {"name": ["Missing data for required field."]})

    def test_update_example(self):
        self.controller.example_service.update_example = MagicMock(return_value={"id": 1, "name": "example"})
        response = self.controller.put(id=1)
        self.assertEqual(response[1], 200)
        self.assertEqual(response[0]["data"]["id"], 1)
        self.assertEqual(response[0]["data"]["name"], "example")

    def test_update_example_not_found(self):
        self.controller.example_service.update_example = MagicMock(return_value=None)
        response = self.controller.put(id=1)
        self.assertEqual(response[1], 404)
        self.assertEqual(response[0]["error"], "Example not found")

    def test_update_example_with_validation_errors(self):
        self.controller.example_schema.validate = MagicMock(
            return_value={"name": ["Missing data for required field."]}
        )
        response = self.controller.put(id=1)
        self.assertEqual(response[1], 400)
        self.assertEqual(response[0]["error"], {"name": ["Missing data for required field."]})

    def test_delete_example(self):
        self.controller.example_service.delete_example = MagicMock(return_value=True)
        response = self.controller.delete(id=1)
        self.assertEqual(response[1], 204)
        self.assertIsNone(response[0])

    def test_delete_example_not_found(self):
        self.controller.example_service.delete_example = MagicMock(return_value=False)
        response = self.controller.delete(id=1)
        self.assertEqual(response[1], 404)
        self.assertEqual(response[0]["error"], "Example not found")
