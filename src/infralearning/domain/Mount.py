import os
import shutil


class Mount:

    def __init__(self, 
                 name:str = 'temp', 
                 directory=os.getcwd()
                ):
        self.root = os.path.join(directory, 'mount')
        self.dir = os.path.join(self.root, name)
        self.log = os.path.join(self.dir, 'log')
        self.input = os.path.join(self.dir, 'input')
        self.results = os.path.join(self.dir, 'result')
        if not os.path.exists(self.root):
            os.mkdir(self.root)


    def create_mount(self):
        os.mkdir(self.dir) if not os.path.exists(self.dir) else None
        os.mkdir(self.log) if not os.path.exists(self.log) else None
        os.mkdir(self.input) if not os.path.exists(self.input) else None
        os.mkdir(self.results) if not os.path.exists(self.results) else None


    def recreate_mount(self):
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)
        self.create_mount()