from abc import abstractmethod


class Model:

    @abstractmethod
    def get_nome(self):
        pass


    @abstractmethod
    def setup_dir(self, mount):
        pass


    @abstractmethod
    def run(self, mount):
        pass