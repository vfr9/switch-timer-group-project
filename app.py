import os
from random import randrange
import json
from dotenv import load_dotenv, find_dotenv
import requests
import flask


app = flask.Flask(__name__)  # name is the module name


load_dotenv(find_dotenv())  # This is to load your API keys from .env



@app.route("/")
def index():
   
    
   
    return flask.render_template(
        "index.html"
       
    )  # passing some variables into the template



























app.run(
    debug=True
)  # I will not need to reload the page each time I make changes with the debug=True