from flask import Flask
from flask import render_template
from flask import request
from wordProccess import WordProcessor


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    wordArray = [] 
    for counter, data in enumerate(request.form.getlist('text')):
        wordArray.append(data)
    for counter, data in enumerate(request.form.getlist('date')):
        wordArray.append(data)
    
    return  WordProcessor().process()

if __name__ == '__main__':
    app.run()