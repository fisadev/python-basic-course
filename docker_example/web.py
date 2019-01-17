from datetime import datetime
from flask import Flask, jsonify


app = Flask(__name__)
start = datetime.now()


@app.route("/")
def home_page():
    return "<h3>Demo web page (server started at {start})</h3>".format(start=start)


@app.route("/save/<thing>/")
def save(thing):
    with open('/data/things.txt', 'a') as things_file:
        things_file.write("saved {thing} at {time}\n".format(thing=thing, time=datetime.now()))
    return "<h3>Saved: {thing}</h3>".format(thing=thing)
