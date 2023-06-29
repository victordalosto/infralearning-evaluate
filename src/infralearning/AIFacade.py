from infralearning.domain.Data import Data
from infralearning.engine.Model import Model
from infralearning.service.MountFactory import MountFactory
from infralearning.service.video_service import VideoService


class AIFacade:

    def __init__(self, model:Model):
        self.model = model
        self.mount_factory = MountFactory()
        self.video = VideoService()


    def run(self, data:Data):
        print('\n\nRunning AI')
        
        print('..Mounting directory: ' + data.name)
        mount = self.mount_factory.of(data = data)
       
        print('..Extracting frames from video: ' + data.path_video)
        self.video.extract_frames(path_video=data.path_video, path_dest_frames=mount.mount_raw)

        print('.. Training model')
        self.model.run(mount)