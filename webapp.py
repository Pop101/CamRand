import time
from flask import Flask, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from waitress import serve
from camrand import RandomImageSource

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per second"]
)

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
        result = source.get_random()
    )

# serve
serve(app,host='0.0.0.0',port=1000)