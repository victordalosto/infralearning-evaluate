class Data:

    def __init__(self, 
                 log:str,
                 path_video:str = None,
                 path_image_folder:str = None,
                 name:str = 'temp',
                 ):
        self.log = log
        self.video = path_video
        self.image = path_image_folder
        self.name = name