import flask

app = flask.FLask(__name__)

@app.route('/')
def switch_timer():
    return flask.render_template('checklist.html')