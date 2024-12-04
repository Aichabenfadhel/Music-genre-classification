from flask import Flask, request, jsonify
import joblib
import librosa
import numpy as np
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/svm/predict": {"origins": "http://localhost:4200"}})

# Load the trained model
model_path = "svm_music_genre.pkl"
model = joblib.load(model_path)

# Define genre labels
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

@app.route("/")
def index():
    return "Music Genre Classification API"

@app.route("/svm/predict", methods=["POST"])
def predict():
    # Check if the file is part of the request
    if "audio_file" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    file = request.files["audio_file"]

    try:
        # Load the audio file
        signal, rate = librosa.load(file, sr=None)
        
        # Extract Mel Spectrogram features
        hop_length = 512
        n_fft = 2048
        n_mels = 128
        S = librosa.feature.melspectrogram(y=signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
        S_DB = librosa.power_to_db(S, ref=np.max)
        S_DB = S_DB.flatten()[:1200]  # Match training dimensions

        # Ensure input is reshaped correctly
        feature = np.array(S_DB).reshape(1, -1)

        # Make prediction
        genre_index = model.predict(feature)[0]
        predicted_genre = genres[genre_index]

        return jsonify({"genre": predicted_genre})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
