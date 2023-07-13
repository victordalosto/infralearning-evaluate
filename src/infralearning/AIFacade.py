from infralearning.domain.Data import Data
from infralearning.domain.Mount import Mount
from infralearning.engine.Model import Model
from infralearning.service.VideoService import VideoService
import os


class AIFacade:

    video_service = VideoService()


    def __init__(self, list_model:Model):
        self.list_models = list_model


    def run(self, data:Data, directory=os.getcwd(), truncate=True):
        print('\n\nRunning AIFacade')
        
        mount = Mount(name=data.name, directory=directory)
        
        if truncate:
            print('..Creating mount')
            mount.recreate_mount()

            print('..Extracting frames from video: ' + data.video)
            self.video_service.extract_frames(path_video=data.video, path_dest_frames=mount.input)

        print('..Using AI models')
        for model in self.list_models:
            print('....model:' + model.get_name())
            model.run(mount)