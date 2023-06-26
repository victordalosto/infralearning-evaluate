import os
import shutil

class mount_service:

    root = os.getcwd()
    mount_root = os.path.join(root, 'mount')


    def __init__(self, name='temp'):
        self.mount_dir = os.path.join(self.mount_root, name)
        self.mount_raw = os.path.join(self.mount_dir, 'raw')
        self.mount_log = os.path.join(self.mount_dir, 'log')
        self.mount_results = os.path.join(self.mount_dir, 'result')


    def create_mount(self):
        if not os.path.exists(self.mount_root):
            os.mkdir(self.mount_root)
        if os.path.exists(self.mount_dir):
            shutil.rmtree(self.mount_dir)
        os.mkdir(self.mount_dir)
        os.mkdir(self.mount_raw)
        os.mkdir(self.mount_log)
        os.mkdir(self.mount_results)
