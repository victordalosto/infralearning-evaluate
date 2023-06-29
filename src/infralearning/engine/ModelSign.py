import os
import shutil
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from infralearning.domain.Mount import Mount


class ModeSign:

    model_identifier = tf.keras.models.load_model("models\\placas_identifier.h5")
    model_classifier = tf.keras.models.load_model("models\\placas_classifier.h5")

    labels_identifier = ['not_null', 'null']
    labels_classifier = ['advertencia', 'educativa', 'indicativa', 'regulamentacao', 'servicos', 'temporaria', 'turistico']


    def run(self, mount:Mount):
        dir_identifier, dir_clasifier = self.__setup_dirs(mount)
        self.__run_identifier(mount.mount_raw, dir_identifier)
        self.__run_classifier(os.path.join(dir_identifier, self.labels_identifier[0]), dir_clasifier)


    def __setup_dirs(self, mount):
        dir_identifier = os.path.join(mount.mount_results, 'identifier')
        dir_clasifier = os.path.join(mount.mount_results, 'classifier')
        shutil.rmtree(dir_identifier) if os.path.exists(dir_identifier) else None
        os.mkdir(dir_identifier)
        shutil.rmtree(dir_clasifier) if os.path.exists(dir_clasifier) else None
        os.mkdir(dir_clasifier)
        for label in self.labels_identifier:
            os.mkdir(os.path.join(dir_identifier, label))
        for label in self.labels_classifier:
            os.mkdir(os.path.join(dir_clasifier, label))
        return dir_identifier, dir_clasifier


    
    def __run_identifier(self, dir_input, dir_output):
        for img in os.listdir(dir_input):
            image_target = os.path.join(dir_input, img)
            image = load_img(image_target, target_size=(256, 256))
            image_array = np.expand_dims((img_to_array(image) / 255.0), axis=0)
            
            predict = self.model_identifier.predict(image_array)[0][0]
            if (predict <= 0.5):
                label = self.labels_identifier[0]
                confidence = np.round((1 - predict) * 100, decimals=0)
            else:
                label = self.labels_identifier[1]
                confidence = np.round(predict * 100, decimals=0)

            src = image_target
            dst = os.path.join(dir_output, 
                               label, 
                               (image_target.replace(dir_input, "")
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
                                            .replace("\\", "")
                                            .replace(".jpg", "_" + str(confidence) + ".jpg")))
            shutil.copy(src, dst)