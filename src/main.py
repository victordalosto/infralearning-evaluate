from infralearning.AIFacade import AIFacade
from infralearning.domain.Data import Data
from infralearning.engine.ModelSign import Model_RoadSign


facade = AIFacade([Model_RoadSign()], frames_per_second=1)


data = Data(name = '415BA048647',
            log = '/media/victor/3201/3201/14_06_2022/16_415BA048647/LogsTrecho.xml', 
            path_video = '/media/victor/3201/3201/14_06_2022/16_415BA048647/videos/camera1/415BA048647.mp4')


facade.run(data=data,truncate=True)