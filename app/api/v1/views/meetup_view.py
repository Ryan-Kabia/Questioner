#from app import app
from flask import Flask, jsonify, request, redirect
from v1.models.models import Meetup

app=Flask(__name__)

@app.route('/meetup',methods = ["POST"])
def create_meetup():
    data = request.get_json()

    id = data["id"]
    createdOn = data["createdOn"]
    location = data["location"]
    happeningOn = data["happeningOn"]
    topic = data["topic"]
    Tags = data["Tags"]

    new_meetup = {
        "id": id,
        "createdOn": createdOn,
        "location": location,
        "happeningOn":happeningOn,
        "topic": topic,
        "Tags": Tags,
    }

    Meetup.append(new_meetup)
    
    return jsonify ({"status":201,"data":[new_meetup]}),201
