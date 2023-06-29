import os
import cv2

class VideoService():

    def extract_frames(self, path_video:str, path_dest_frames:str):
        video = cv2.VideoCapture(path_video)
        success, image = video.read()
        
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_number = 0
        
        while success:
            timing = frame_number % int(round(fps))
            if (timing == 0):
                cv2.imwrite(os.path.join(path_dest_frames, "%d.jpg" %  (frame_number / int(round(fps)))), image)
            success, image = video.read()
            frame_number += 1
        video.release()