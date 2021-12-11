from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    texte = request.form['texte']
    model = SentimentIntensityAnalyzer()
    score = ((model.polarity_scores(str(texte))))['compound']

    if(score > 0):
        label = 'This sentence is positive'
    elif(score == 0):
        label = 'This sentence is neutral'
    else:
        label = 'This sentence is negative'
        
    return render_template('index.html', prediction=label, sentcolor=color)





   


    #if pred == 1:
        #color = green, prediction = 'Positiv'
    #color = '#f64c46'

    