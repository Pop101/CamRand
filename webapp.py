import time
import os
import subprocess
from flask import Flask, jsonify, render_template
from waitress import serve

from camrand import hash_to_int, numberToBase
from camrand import RandomImageSource

import pyximport; pyximport.install()

FPS = 10
RESOLUTION = "440x300"

# Take constant images in the background
subprocess.Popen(['ffmpeg', '-y', '-f', 'video4linux2', '-i', '/dev/video0', '-s', str(RESOLUTION), '-vf', f'fps={FPS}', '-update', '1', 'static.jpg'])

app = Flask(__name__)

source = RandomImageSource(take_picture=False)
source.last_call = time.time()

def test():
    last_seed, t = source.last_random, time.time()
    number = hash_to_int(source.get_raw_int() - last_seed)
    subprocess.call('echo', str(number),  '>> testing')
    return subprocess.call("ent testing").read()
    

# GET PUT (override, immuteable) POST (new) DELETE
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/random')
def rand():    
    last_seed, t = source.last_random, time.time()
    
    # ensure enough time has passed for a new frame to have arrived
    to_wait = ( 1.08 * 1/FPS ) - (t - source.last_call) # add an 8% threshold to account for ffmpeg image processing time
    if to_wait > 0:
        time.sleep(to_wait)
    
    source.last_call = time.time()
    return jsonify(
        status = 'OK',
        origin = source.last_call,
        result = hash_to_int(source.get_raw_int() - last_seed),
        testresult = test()
    )

# serve
serve(app, host = '0.0.0.0', port = 1000)