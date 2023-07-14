from infralearning.domain.Data import Data
from infralearning.domain.Mount import Mount
from infralearning.engine.Model import Model
from infralearning.service.VideoService import VideoService
import os


class AIFacade:


    def __init__(self, list_models:Model, frames_per_second=1):
        self.list_models = list_models
        self.video_service = VideoService(frames_per_second)


    def run(self, data:Data, directory=os.getcwd(), truncate=True):

        print('\n\nRunning AI Facade')
        
        mount = Mount(name=data.name, directory=directory)
        
        if not truncate:
            print('.. Creating mount')
            mount.create_mount()
        else:
            print('.. Clearing mount')
            mount.recreate_mount()

        if truncate and data.video is not None:
            print('.. Extracting frames from video: ' + data.video)
            self.video_service.extract_frames(path_video=data.video, path_dest_frames=mount.input)

        if data.image is not None:
            print('.. Making mount input as link shortcut: ' + data.image)
            mount.input = data.image

        print('.. Evaluating using AI models')
        for model in self.list_models:
            print('.... Model:' + model.get_name())
            model.run(input_path=mount.input, output_path=mount.results)
        
        return mount