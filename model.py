from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


class Model:

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def evaluate(self, image_url):
        image = Image.open(image_url)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image_array
        prediction = self.model.predict(self.data)
        # print(prediction)
        if prediction[0][0] > prediction[0][1]:
            return 'Enceinte', f'{prediction[0][0]*100} %'
        else:
            return 'Pas enceinte', f'{prediction[0][1]*100} %'
