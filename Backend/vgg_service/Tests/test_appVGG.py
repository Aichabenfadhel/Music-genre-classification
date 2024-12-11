import pytest
import os
import io
from io import BytesIO
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app  


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/vgg')
    data = rv.get_json()
    assert rv.status_code == 200
    assert 'message' in data
    assert data['message'] == "VGG19 Flask API is running."


def test_vgg_valid_file(client):
    test_file_path = os.path.join(os.path.dirname(__file__), 'test.png')  
    with open(test_file_path, 'rb') as file:
        rv = client.post('/vgg/predict', data={'file': (file, 'test.png')}, content_type='multipart/form-data')
        assert rv.status_code == 200
        data = rv.get_json()
        assert 'predictions' in data


def test_vgg_no_file(client):
    rv = client.post('/vgg/predict')
    assert rv.status_code == 400
    data = rv.get_json()
    assert 'error' in data
