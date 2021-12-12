from flask import Flask, render_template, request, redirect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
from string import punctuation

nltk.download('stopwords')
stop_words = stopwords.words('english')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "GET":
        return redirect('/')
        
    if request.method == 'POST':
        texte = [str(x) for x in request.form.values()]
        
        no_punc = []
        for w in texte:
            if w not in punctuation:
                no_punc.append(w)

        lower_text = [x.lower() for x in no_punc]

        final_words = []
        for w in lower_text:
            if w not in stop_words:
                final_words.append(w)

        to_process = " ".join([w for w in final_words])
            
        model = SentimentIntensityAnalyzer()
        score = model.polarity_scores(to_process)["compound"]
        
        if score > 0 : 
            pred = "The sentence is overall positive."
            color = "#a9ecbc"
        if score < 0 :
            pred = "The sentence is overall negative."
            color = "#C64444"
        if score == 0 : 
            pred = "The sentence is overall neutral."
            color = "#cdccff"
        
        return render_template('index.html', prediction=pred, sentcolor=color)
