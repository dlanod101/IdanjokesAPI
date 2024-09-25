from flask import Flask, request, jsonify, render_template, url_for
from random import randint
import json, os

app = Flask(__name__)

img = os.path.join('static', 'Image')

@app.route('/')
def home():
    file = os.path.join(img, 'idan.png')
    return render_template('home.html', image=file)

@app.route('/jokes/<id>')
def joke(id):
    
    with open("jokes.json", "r") as file:
        jokes = json.load(file)

    
    return jsonify(jokes[int(id)]), 200

@app.route('/jokes/random')
def random_joke():
    
    with open("jokes.json", "r") as file:
        jokes = json.load(file)

    random_joke = jokes[int(randint(0, 50))]
    
    return jsonify(random_joke), 200

if __name__ == '__main__':
    app.run(debug=True)
 