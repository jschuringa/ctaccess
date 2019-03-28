from flask import Flask, render_template
from tracker import train
app = Flask(__name__)

@app.route("/")
def home():
    track = train.TrainTracker("key")
    routes = track.get_routes()
    return render_template('trainroutes.html', routes=routes)