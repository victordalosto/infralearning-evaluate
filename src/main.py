from infralearning.AIFacade import AIFacade
from infralearning.domain.Data import Data
from infralearning.engine.Model import Model
from infralearning.engine.ModelSign import ModeSign


models = Model.of([ModeSign()])
facade = AIFacade(models)


data = Data(name = '0_010DF025000',
            path_log = 'D:\\temp\\4100\\16_05_2023\\0_010DF025000\\LogsTrecho.xml', 
            path_video = 'D:\\temp\\4100\\16_05_2023\\0_010DF025000\\videos\\camera1\\010DF025000.mp4')


facade.run(data)