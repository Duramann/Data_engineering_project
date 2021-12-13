import web_app
import pytest
import nltk
import vaderSentiment
import string
import pandas as pd
import time
import random

## Create a pytest fixture that configure the application for testing. 
@pytest.fixture
def client():
    app = web_app.app
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

## Test if the site is working for "/" route and "/predict" post route.
## Test if the get route for "/predict" redirect corretly.
def test_status(client):
    mp = client.get("/")
    assert mp.status_code == 200
    pred = client.get("/predict")
    assert pred.status_code == 302
    predicted = client.post('/predict', data={"sentence":"Today was a good day!"})
    assert predicted.status_code == 200

## Test if the site returns the correct answer when sending sentence to analyse.
def test_predic(client):
    pred_pos = client.post('/predict', data={"sentence":"Today was a good day!"})
    assert b'positive' in pred_pos.data
    pred_neg = client.post('/predict', data={"sentence":"Today was a bad day!"})
    assert b'negative' in pred_neg.data
    pred_neut = client.post('/predict', data={"sentence":"Dogs are animals."})
    assert b'neutral' in pred_neut.data
    pred_fr = client.post('/predict', data={"sentence":"Cette phrase est en Français"})
    assert b'neutral' in pred_fr.data
    pred_int = client.post('/predict', data={"sentence":"12 54 52 35"})
    assert b'neutral' in pred_int.data

## Test if the average response time of the home page is below 100ms.
def test_stress_home(client):
    recorded_time = []
    for i in range(1000):
        start = time.time()
        client.get('/')
        end = time.time()
        recorded_time.append(start-end*1000)
    avg_time = sum(recorded_time)/len(recorded_time)
    assert avg_time < 100

## Test if the average response time of a prediction is below 100ms.
def test_stress_prediction(client):
    recorded_time = []
    data = pd.read_csv('data/labelled_sentence.csv', sep=";", header=0)
    for i in range(1000):
        index = random.randint(0, len(data)-1)
        start = time.time()
        client.post('/predict', data={"sentence":data['sentence'][index]})
        end = time.time()
        recorded_time.append(start-end*1000)
    avg_time = sum(recorded_time)/len(recorded_time)
    assert avg_time < 100

## Test if the accuracy of our back-end model is above or equal to 70%.
def test_accuracy(client):
    correct_values = 0
    data = pd.read_csv('data/labelled_sentence.csv', sep=";", header=0)
    for i in range(len(data)):
        pred = client.post('/predict', data={"sentence":data['sentence'][i]})
        if b'positive' in pred.data and data['label'][i]==1:
            correct_values +=1
        if b'negative' in pred.data and data['label'][i]==0:
            correct_values+=1
    accuracy = correct_values/len(data)
    assert accuracy >= 0.7
        

