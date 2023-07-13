import os
import cv2
from math import floor


class VideoService():

    desired_frames_per_second = 9


    def extract_frames(self, 
                       path_video:str, 
                       path_dest_frames:str
                       ):
        video = cv2.VideoCapture(path_video)
        success, image = video.read()

        fps = int(round(video.get(cv2.CAP_PROP_FPS)))
        step_frames = min(self.desired_frames_per_second, fps)
        interval_frames = max(1, floor(fps/step_frames))

        n_frame = 0
        while success:
            if (n_frame%interval_frames == 0):
                second = floor(n_frame / fps)
                count = n_frame % fps
                name = str(second) + "_" + str(count) + ".jpg"
                cv2.imwrite(os.path.join(path_dest_frames, name), image)
            success, image = video.read()
            n_frame += 1
        video.release()