from app.models.example_model import ClientModel


class Service:
    def __init__(self):
        self.model = ClientModel()

    # def get_all_examples(self):
    #     examples = self.model.get_all()
    #     return examples

    def get_by_id(self, typeId, customId):
        response = self.model.get_by_id(typeId, customId)
        return response

    # def create(self, data):
    #     response = self.model.save(data)
    #     return response

    # def update_example(self, example_id, example_data):
    #     example = self.model.update(example_id, example_data)
    #     return example

    # def delete_example(self, id):
    #     responde = self.model.delete(id)
    #     return responde
