from datetime import datetime
from flask import Flask


app = Flask(__name__)
start = datetime.now()


@app.route("/")
def home_page():
    return "<h1>Demo web page (server started at {start})</h1>".format(start=start)


@app.route("/save/<thing>/")
def save(thing):
    with open('/data/things.txt', 'a') as things_file:
        things_file.write("saved {thing} at {time}\n".format(thing=thing, time=datetime.now()))
    return "<h1>Saved: {thing}</h1>".format(thing=thing)
