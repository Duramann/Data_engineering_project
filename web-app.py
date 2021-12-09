from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    texte = [str(x) for x in request.form.values()]
    #if pred == 1:
        #color = green, prediction = 'Positiv'
    color = '#f64c46'
    
    return render_template('index.html', prediction='Not yet implemented !', sentcolor=color)