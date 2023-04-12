from flask import Flask
from flask import render_template
from flask import request
from main import main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    word = [] 
    for counter, data in enumerate(request.form.getlist('text')):
        word.append(data)
    for counter, data in enumerate(request.form.getlist('date')):
        word.append(data)
    # print(word)
    main(word)
    return 'test'

if __name__ == '__main__':
    app.run()