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
        print('\n\nRunning AI')
        
        print('..Mounting directory: ' + data.name)
        mount = Mount(name=data.name, 
                      directory=directory, 
                      truncate=truncate)
       
        print('..Extracting frames from video: ' + data.video)
        self.video_service.extract_frames(path_video=data.video, path_dest_frames=mount.input)

        print('.. Training model')
        for model in self.list_models:
            model.run(mount)