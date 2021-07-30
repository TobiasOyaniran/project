# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/choose_activity")
def choose_activity():
    if 1:
        print("We recommend browsing through some memes!")
    return "Choose an activity!"