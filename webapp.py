import time
from flask import Flask, jsonify, render_template
from waitress import serve
from camrand import RandomImageSource
import pyximport; pyximport.install()


app = Flask(__name__)

source = RandomImageSource()
source.last_call = time.time()

# GET PUT (override, immuteable) POST (new) DELETE
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/random')
def new_rand():
    source.last_call = time.time()
    return jsonify(
        status = "OK",
        origin = source.last_call,
        result = source.get_seed()
    )

# serve
serve(app,host='0.0.0.0',port=1000)