import os
import shutil

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from infralearning.engine.Model import Model


class Model_RoadSign(Model):

    model_detection = tf.keras.models.load_model("models/sign_detection.h5")
    model_classifier = tf.keras.models.load_model("models/sign_classification.h5")

    labels_detection = ['not_null', 'null']
    labels_classifier = ['advertencia', 'educativa', 'indicativa', 'regulamentacao', 'servicos', 'turistico']


    def run(self, input_path, output_path):
        dir_detection, dir_classifier = self.setup_dir(output_path)
        self.__run_detection(input_path, dir_detection)
        self.__run_classifier(os.path.join(dir_detection, self.labels_detection[0]), dir_classifier)



    def setup_dir(self, path):
        dir = os.path.join(path, self.get_name())
        dir_detection = os.path.join(dir, 'identifier')
        dir_classifier = os.path.join(dir, 'classifier')
        shutil.rmtree(dir) if os.path.exists(dir) else None
        os.mkdir(dir)
        os.mkdir(dir_detection)
        os.mkdir(dir_classifier)
        for label_detection in self.labels_detection:
            os.mkdir(os.path.join(dir_detection, label_detection))
        for label_classifier in self.labels_classifier:
            os.mkdir(os.path.join(dir_classifier, label_classifier))
        return dir_detection, dir_classifier


    
    def __run_detection(self, dir_input, dir_output):
        list_predictions = [[],[]]
        for img in os.listdir(dir_input):
            image_target = os.path.join(dir_input, img)
            image = load_img(image_target, target_size=(256, 256))
            image_array = np.expand_dims((img_to_array(image) / 255.0), axis=0)
            
            predict = self.model_detection.predict(image_array)[0][0]
            if (predict < 0.5):
                label = self.labels_detection[0]
                confidence = np.round((1 - predict) * 100, decimals=0)
                list_predictions.append(confidence)
            else:
                label = self.labels_detection[1]
                confidence = np.round(predict * 100, decimals=0)

            src = image_target
            dst = os.path.join(dir_output, 
                               label, 
                               (image_target.replace(dir_input, "")
                                            .replace("/", "")
                                            .replace("\\", "")
                                            .replace(".jpg", "_" + str(confidence) + ".jpg")))
            shutil.copy(src, dst)


    
    def __run_classifier(self, dir_input, dir_output):
        for img in os.listdir(dir_input):
            image_target = os.path.join(dir_input, img)
            image = load_img(image_target, target_size=(256, 256))
            image_array = np.expand_dims((img_to_array(image) / 255.0), axis=0)
            
            predict = self.model_classifier.predict(image_array)
            label = self.labels_classifier[np.argmax(predict)]
            confidence = np.round(predict[0, np.argmax(predict)] * 100, decimals=1)

            src = image_target
            dst = os.path.join(dir_output, 
                               label, 
                               (image_target.replace(dir_input, "")
                                            .replace("/", "")
                                            .replace("\\", "")
                                            .replace(".jpg", "_" + str(confidence) + ".jpg")))
            shutil.copy(src, dst)



    def get_name(self):
        return "sign"