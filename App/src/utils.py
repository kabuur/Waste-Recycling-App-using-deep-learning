# predictor/utils.py

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your pre-trained model
model = load_model('model.h5')

def predict_image(img_path):
    # img = image.load_img(img_path, target_size=(224, 224))  # Adjust target_size as needed
    # img_array = image.img_to_array(img)
    # img_array = np.expand_dims(img_array, axis=0) / 255.0
    # prediction = model.predict(img_array)
    # return prediction
    img = image.load_img(img_path, target_size=(224, 224))
    img = img.resize((224, 224))  # Resize to the input shape your model expects
    img = np.array(img) / 255.0  # Normalize to [0, 1] range
    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)
    
    return  predicted_class[0] 
    

      



