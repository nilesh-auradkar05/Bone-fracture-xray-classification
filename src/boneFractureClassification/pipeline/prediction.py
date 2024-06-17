import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from boneFractureClassification.utils.common import select_recent_model

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        recent_model = select_recent_model()
        model = load_model(os.path.join("artifacts","training",f"{recent_model}"))
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(528, 528))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        
        if result[0] == 1:
            prediction = "Fracture"
            return [{"image": prediction}]
        else:
            prediction = "No Fracture"
            return [{"image": prediction}]