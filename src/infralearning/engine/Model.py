from abc import abstractmethod

from infralearning.domain.Mount import Mount


class Model:


    @abstractmethod
    def get_name(self) -> str:
        pass


    @abstractmethod
    def setup_dir(self, path):
        pass


    @abstractmethod
    def run(self, input_path, output_path) -> Mount:
        pass