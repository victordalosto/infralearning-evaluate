from infralearning.domain.mount import mount

class mount_factory:

    def of(self, data):
        instance = mount(data.name)
        return instance