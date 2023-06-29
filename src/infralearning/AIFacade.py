from infralearning.service.MountFactory import MountFactory
from infralearning.service.video_service import VideoService


class AIFacade:

    def __init__(self, model):
        self.model = model
        self.mount_factory = MountFactory()
        self.video = VideoService()


    def run(self, data):
        mount = self.mount_factory.of(data = data)
        self.video.extract_frames(path_video=data.path_video, path_dest_frames=mount.mount_raw)
        self.model.run(mount)