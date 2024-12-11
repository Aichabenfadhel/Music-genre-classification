
import io
import sys
import os
import pytest
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from app import app

@pytest.fixture
def client():
    """Set up a Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Music Genre Classification API"

def test_predict_no_file(client):
    """Test predict route with no file"""
    response = client.post("/svm/predict")
    assert response.status_code == 400
    assert response.get_json() == {"error": "No audio file provided"}

def test_predict_invalid_file(client):
    """Test predict route with an invalid file"""
    data = {'audio_file': (io.BytesIO(b"fake audio data"), 'test.mp3')}
    response = client.post("/svm/predict", data=data)
    assert response.status_code == 500
    assert "error" in response.get_json()

