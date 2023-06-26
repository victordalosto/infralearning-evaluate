from infralearning.service.mount_service import mount_service
from infralearning.service.video_service import video_service


class data:

    def __init__(self, path_video, path_log, name = 'temp'):
        self.name = name
        self.path_video = path_video
        self.path_log = path_log
        self.mount = mount_service(name = self.name)
