
class model:

    def __init__(self, models):
        self.models = models


    def run(self, data):
        for model in self.models:
            model.run(data)