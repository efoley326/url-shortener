from flask import Flask

app = Flask(__name__)

@app.route("/")
def do_things_when_you_want_me_to():
    return "<p>Like controlla</p>"