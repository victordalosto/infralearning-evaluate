from infralearning.service.video_service import video_service


class ai_facade:


    def run(self, data):
        video = video_service()
        data.mount.create_mount()
        video.extract_frames(data.path_video, data.mount.mount_raw)