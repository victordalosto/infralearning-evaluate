from infralearning.domain.Data import Data


data = Data(name = '418BA000000',
            log = '/media/victor/3201/3201/12_06_2022/1_418BA000000/LogsTrecho.xml', 
            path_video = '/media/victor/3201/3201/12_06_2022/1_418BA000000/videos/camera1/418BA000000.mp4')

print(data.image)