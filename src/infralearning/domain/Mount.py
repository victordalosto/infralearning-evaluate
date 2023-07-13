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


    def recreate_mount(self):
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)
        os.mkdir(self.dir)
        os.mkdir(self.input)
        os.mkdir(self.log)
        os.mkdir(self.results)


    def get_input(self):
        return self.input