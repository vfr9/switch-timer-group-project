import flask

app = flask.Flask(__name__)

@app.route('/')
def switch_timer():
    return flask.render_template('checklist.html')

app.run()