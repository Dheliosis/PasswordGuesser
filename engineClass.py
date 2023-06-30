from flask import Flask
from flask import render_template
from flask import request
from wordProcess import WordProcessor


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    word_array = [] 
    for counter, data in enumerate(request.form.getlist('text')):
        word_array.append(data)
    for counter, data in enumerate(request.form.getlist('date')):
        word_array.append(data)
    
    result = WordProcessor(word_array).process(word_array)
    print("I have found", result.__len__(), "possibilities")

    return result

if __name__ == '__main__':
    app.run()