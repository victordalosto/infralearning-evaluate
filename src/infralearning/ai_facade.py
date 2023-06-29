from infralearning.service.mount_factory import mount_factory
from infralearning.service.video_service import video_service


class ai_facade:

    def __init__(self, model):
        self.model = model
        self.mount_factory = mount_factory()
        self.video = video_service()


    def run(self, data):
        mount = self.mount_factory.of(data = data)
        self.video.extract_frames(path_video=data.path_video, path_dest_frames=mount.mount_raw)
        self.model.run(mount)