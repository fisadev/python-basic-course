from flask import Flask
app = Flask(__name__)


@app.route("/home/")
def home_page():
    return "<h3>Demo web page</h3>"

@app.route("/user/<user_id>/")
def view_user(user_id):
    return "<h3>Viewing the user: {}</h3>".format(user_id)
