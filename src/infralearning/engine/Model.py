from abc import abstractmethod


class Model:


    @abstractmethod
    def get_nome(self):
        pass


    @abstractmethod
    def setup_dir(self, path):
        pass


    @abstractmethod
    def run(self, input_path, output_path):
        pass