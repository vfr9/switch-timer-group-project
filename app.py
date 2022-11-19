import os
from random import randrange
import json
from dotenv import load_dotenv, find_dotenv
import requests
import flask
import random

app = flask.Flask(__name__)  # name is the module name

load_dotenv(find_dotenv())  # This is to load your API keys from .env

@app.route("/break")
def break_screen():
    BOBS_BURGERS_REQUEST = (
        "https://bobsburgers-api.herokuapp.com/episodes/"
        + str(random.choice([randrange(1, 238)]))
    )
    response = requests.get(BOBS_BURGERS_REQUEST)
    json_data = response.json()
    show_data = json_data
    tv_url = show_data["episodeUrl"]
    tv_title = show_data["name"]
    tv_season = show_data["season"]
    tv_episode = show_data["episode"]

    return flask.render_template(
        "break.html",
        showurl=tv_url,
        title=tv_title,
        season=str(tv_season),
        episode=str(tv_episode),
    )

@app.route("/")
def index():
    return flask.render_template(
        "index.html"
    )  # passing some variables into the template


app.run(
    debug=True
)  # I will not need to reload the page each time I make changes with the debug=True
