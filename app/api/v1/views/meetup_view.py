from flask import Flask, jsonify, request, Blueprint
from app.api.v1.models.models import Meetup,Question
from random import *

#app=Flask(__name__)
mod1 = Blueprint('api', __name__)

@mod1.route('/meetups/upcoming/')
def all_meetups():
    return jsonify({"status": 200, "data": Meetup}), 200


@mod1.route('/meetups/<meetup_id>')
def specific_meetups(meetup_id):
    for entry in Meetup:
        if entry["id"] == int(meetup_id):
            return jsonify({"status": 200, "data": entry}), 200

    return jsonify ({"status":404,"data":"entry cannot be found"}),404


@mod1.route('/meetups',methods = ["POST"])
def create_meetup():
    data = request.get_json()

    last_id=Meetup[-1]["id"]
    inc_id= last_id+1

    id = inc_id        
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


@mod1.route('/questions', methods=["POST"])
def create_question():
    data = request.get_json()

    last_id = Question[-1]["id"]
    inc_id = last_id+1

    id = inc_id
    createdOn = data["createdOn"]
    createdBy = data["createdBy"]
    meetup = data["meetup"]
    title = data["title"]
    votes = randint(0,50)

    new_question = {
        "id": id,
        "createdOn": createdOn,
        "createdBy": createdBy,
        "meetup": meetup,
        "title": title,
        "votes": votes,
    }

    Question.append(new_question)

    return jsonify({"status": 201, "data": [new_question]}), 201
