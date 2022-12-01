import os
from random import randrange
import json
from dotenv import load_dotenv, find_dotenv
import requests
from flask import Flask, render_template, request
import random
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)  # name is the module name, it is where the app should start running



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sL74217513@localhost/tim'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)





class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(80), unique=True, nullable=False)

    #def __repr__(self): # this will give it a string representation of itself
     #   return f'Event: {self.activity}' # this f string allows you to inject python variables

    def __init__(self, activity):
        self.activity= activity
        



    





load_dotenv(find_dotenv())  # This is to load your API keys from .env

@app.route("/break")
def break_screen():
    BOBS_BURGERS_REQUEST = (
        "https://bobsburgers-api.herokuapp.com/episodes/"
        + str(random.choice([randrange(1, 238)]))
    )
    BB_CHARACTER_REQUEST = (
        "https://bobsburgers-api.herokuapp.com/characters/"
        + str(random.choice([randrange(1, 500)]))
    )
    response = requests.get(BOBS_BURGERS_REQUEST)
    json_data = response.json()
    show_data = json_data
    tv_url = show_data["episodeUrl"]
    tv_title = show_data["name"]
    tv_season = show_data["season"]
    tv_episode = show_data["episode"]
    
    response = requests.get(BB_CHARACTER_REQUEST)
    json_data = response.json()
    char_data = json_data
    image_url = char_data["image"]

    return render_template(
        "break.html",
        showurl=tv_url,
        title=tv_title,
        season=str(tv_season),
        episode=str(tv_episode),
        image = image_url
    )

@app.route("/work")
def work_screen():
    return render_template("work.html")

@app.route("/")
def index():
    return render_template("index.html")
#def home():
#    return '<a href="/addperson"><button> Click here </button></a>'
#  #main page
    #return flask.redirect(flask.url_for("break_screen")) #break page


@app.route("/addperson")
def addperson():
    return render_template("index.html")

@app.route("/personadd", methods=['POST'])
def personadd():
    activity = request.form["activity"]
    entry = Event(activity)
#   db.session.add(entry)
#    db.session.commit()

    return render_template("index.html")






if __name__ == '__main__':
#    with app.app_context():
#        db.create_all()
        app.run(
            debug=True
        )  # I will not need to reload the page each time I make changes with the debug=True
