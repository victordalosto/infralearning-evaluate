from infralearning.ai_facade import ai_facade
from infralearning.domain.data import data
from infralearning.engine.model import model
from infralearning.engine.model_sign import model_sign


models = model([model_sign()])
aifacade = ai_facade(models)


dado = data(name = '0_010DF025000',
            path_log = 'D:\\temp\\4100\\16_05_2023\\0_010DF025000\\LogsTrecho.xml', 
            path_video = 'D:\\temp\\4100\\16_05_2023\\0_010DF025000\\videos\\camera1\\010DF025000.mp4')


aifacade.run(dado)