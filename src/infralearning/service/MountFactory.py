from infralearning.domain.Mount import Mount

class MountFactory:

    def of(self, data):
        instance = Mount(data.name)
        return instance