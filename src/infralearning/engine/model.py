
class Model:

    def __init__(self, models):
        self.models = models


    def of(models):
        return Model(models)


    def run(self, data):
        for model in self.models:
            model.run(data)