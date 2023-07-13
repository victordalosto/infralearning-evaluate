from infralearning.AIFacade import AIFacade
from infralearning.domain.Data import Data
from infralearning.engine.ModelSign import Model_RoadSign


facade = AIFacade([Model_RoadSign()])


data = Data(name = '418BA000000',
            log = '/media/victor/3201/3201/12_06_2022/1_418BA000000/LogsTrecho.xml', 
            video = '/media/victor/3201/3201/12_06_2022/1_418BA000000/videos/camera1/418BA000000.mp4')


facade.run(data=data)