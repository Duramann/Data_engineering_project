import requests
import web_app
import pytest
import nltk
import vaderSentiment
import string

@pytest.fixture
def client():
    app = web_app.app
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_status(client):
    mp = client.get("/")
    assert mp.status_code == 200
    red = client.get("/predict")
    assert mp.status_code == 200

def test_predic(client):
    pred1 = client.post('/predict', data={"sentence":"Today was a good day!"})
    assert b'positive' in pred1.data
    pred2 = client.post('/predict', data={"sentence":"Today was a bad day!"})
    assert b'negative' in pred2.data
    pred3 = client.post('/predict', data={"sentence":"Dogs are animals."})
    assert b'neutral' in pred3.data

#def test_stress(client):
#    time = []
#    for i in range(1000):
#        res = client.get('/')
#        time.append(res.elapsed.total_seconds()*1000)
#    avg_time = sm(time)/len(time)
#    assert avg_time < 100