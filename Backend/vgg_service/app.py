from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import os
from io import BytesIO
from flask_cors import CORS 


app = Flask(__name__)

CORS(app)
CORS(app, resources={r"/vgg/predict": {"origins": "http://localhost:4200"}})

MODEL_PATH = './vgg19_music_genre_classification.h5'  
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
    print("Custom VGG19 model loaded successfully.")
else:
    model = VGG19(weights='imagenet')
    print("Pretrained VGG19 model loaded successfully.")

IMG_SIZE = (224, 224)

GENRE_MAP = {
    0: 'blues',
    1: 'classical',
    2: 'country',
    3: 'disco',
    4: 'hiphop',
    5: 'jazz',
    6: 'metal',
    7: 'pop',
    8: 'reggae',
    9: 'rock',
}

@app.route('/vgg')
def home():
    return jsonify({"message": "VGG19 Flask API is running."})

@app.route('/vgg/predict', methods=['POST'])
def predict():
    """Endpoint to make predictions."""
   
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided. Please upload an image.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading.'}), 400

    try:
        
        image = load_img(BytesIO(file.read()), target_size=IMG_SIZE)

        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        predictions = model.predict(image_array)

        if model.input_shape[1:] == (224, 224, 3) and predictions.shape[1] == 1000:
            
            decoded_predictions = decode_predictions(predictions, top=3)
            response = [
                {"genre": pred[1], "description": pred[1], "confidence": float(pred[2])}
                for pred in decoded_predictions[0]
            ]
        else:
            
            predicted_class_index = np.argmax(predictions, axis=1).tolist()[0]
            genre_name = GENRE_MAP.get(predicted_class_index, 'Unknown')  
            confidence = float(predictions[0][predicted_class_index])
            response = {
                "predicted_genre": genre_name,
                "confidence": confidence
            } 

        return jsonify({"predictions": response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
