from flask import Flask, jsonify, request, Blueprint
from app.api.v1.models.models import Meetup,Question,Rsvp
from app.api.v1.utils.validate import Validate
from random import randint

#app=Flask(__name__)
mod1 = Blueprint('api', __name__)
vldr = Validate()

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
    if vldr.check_empty(data["createdOn"], data["location"], data["happeningOn"], data["topic"], data["Tags"]) == False:
        return jsonify({"Message":"empty field"})
    if vldr.check_date(data["createdOn"], data["happeningOn"]) == False:
        return jsonify({"Message": "Bad date format"})
    if vldr.check_valid_date(data["createdOn"], data["happeningOn"]) == False:
        return jsonify({"Message": "Date cannot be less than today"})

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

    if vldr.check_empty(data["createdOn"], data["createdBy"], data["meetup"], data["title"], data["body"]) == False:
        return jsonify({"Message": "empty field"})
    if vldr.check_date(data["createdOn"]) == False:
        return jsonify({"Message": "Bad date format"})
    if vldr.check_valid_date(data["createdOn"]) == False:
        return jsonify({"Message": "Date cannot be less than today"})

    id = inc_id
    createdOn = data["createdOn"]
    createdBy = data["createdBy"]
    meetup = data["meetup"]
    title = data["title"]
    body = data["body"]
    votes = 0

    new_question = {
        "id": id,
        "createdOn": createdOn,
        "createdBy": createdBy,
        "meetup": meetup,
        "title": title,
        "body":body,
        "votes": votes,
    }

    Question.append(new_question)

    return jsonify({"status": 201, "data": [new_question]}), 201


@mod1.route('/meetups/<meetup_id>/rsvp', methods=["POST"])
def rsvp(meetup_id):

    data = request.get_json()

    last_id = Rsvp[-1]["id"]
    inc_id = last_id+1

    if vldr.check_empty(data["user"], data["responce"]) == False:
        return jsonify({"Message": "empty field"})
    if vldr.check_responce(data["responce"]) == False:
        return jsonify({"Message": "Limit Answers to:Yes, No or Maybe"})

    id = inc_id
    meetup = int(meetup_id)
    user = data["user"]
    responce = data["responce"]

    new_rsvp = {
        "id":id,
        "meetup":meetup,
        "user":user,
        "responce":responce
    }

    Rsvp.append(new_rsvp)

    for entry in Meetup:
        if entry["id"] == int(meetup_id):
            topic= entry["topic"]
            break
    
    rtrn_obj ={
        "meetup":meetup,
        "topic": topic,
        "responce":responce
    }
    return jsonify({"status": 201, "data": [rtrn_obj]}), 201

@mod1.route('/questions/<question_id>/upvote', methods=["PATCH"])
def upvote(question_id):
    for entry in Question:
        if entry["id"] == int(question_id):
            meetup = entry["meetup"]
            title = entry["title"]
            body = entry["body"]
            votes = entry["votes"]+1
            break
    
    rtrn_obj = {"meetup":meetup,
                "title":title,
                "body":body,
                "votes":votes
                }
    return jsonify({"status": 201, "data": [rtrn_obj]}), 201

@mod1.route('/questions/<question_id>/downvote', methods=["PATCH"])
def downvote(question_id):
    for entry in Question:
        if entry["id"] == int(question_id):
            meetup = entry["meetup"]
            title = entry["title"]
            body = entry["body"]
            votes = entry["votes"]-1
            break
    
    rtrn_obj = {"meetup":meetup,
                "title":title,
                "body":body,
                "votes":votes
                }
    return jsonify({"status": 201, "data": [rtrn_obj]}), 201
