import requests
import web_app
import pytest
import time

def test_url():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    response = requests.get("http://localhost:5000/predict")
    assert response.status_code == 200

def test_input():
    response = requests.post("http://localhost:5000/predict", data="This is a test sentence")
    answer = response.text
    assert response.status_code == 200
    assert 'Not yet implemented !' in answer

    
def test_stress():
    time = []
    for i in range(1000):
        response = requests.get("http://localhost:5000")
        time.append(response.elapsed.total_seconds()*1000)
    avg_time = sum(time)/len(time)
    assert avg_time < 100