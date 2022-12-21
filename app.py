# @copyright T.Mallet 
# @file app.py

from flask import Flask, render_template

import time

app = Flask(__name__)


@app.route('/')
def default():
    return render_template('loading.html')


@app.route('/loading/')
def loading():
    time.sleep(5)  # time consuming functions
    return render_template("loaded.html")
