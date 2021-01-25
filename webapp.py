import time
from flask import Flask, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from apscheduler.schedulers.background import BackgroundScheduler

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
        result = int(time.time())
    )

# keep old_rand fresh
def quick_update():
    source.last_call = time.time()
    source.get_seed()
    
apsched = BackgroundScheduler()
apsched.start()
apsched.add_job(quick_update, 'interval', seconds=10)

# serve
serve(app,host='0.0.0.0',port=8080)