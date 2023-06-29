from infralearning.domain.Data import Data
from infralearning.domain.Mount import Mount

class MountFactory:

    def of(self, data:Data):
        instance = Mount(data.name)
        return instance