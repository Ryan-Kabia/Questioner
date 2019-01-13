from flask import Flask, jsonify, request, Blueprint
from app.api.v1.models.models import Meetups,Questions,Rsvps,Comments
from app.api.v1.utils.validate import Validate

#app=Flask(__name__)
mod2 = Blueprint('api2', __name__)

vldr = Validate()

@mod2.route('/meetups/upcoming/')
def all_meetups():
    return jsonify({"status": 200, "data": Meetups}), 200


@mod2.route('/meetups/<meetup_id>')
def specific_meetups(meetup_id):
    for entry in Meetups:
        if entry["id"] == int(meetup_id):
            return jsonify({"status": 200, "data": entry}), 200

    return jsonify ({"status":404,"data":"entry cannot be found"}),404


@mod2.route('/meetups',methods = ["POST"])
def create_meetup():
    data = request.get_json()

    last_id=Meetups[-1]["id"]
    inc_id= last_id+1

    id = inc_id 
    if vldr.check_empty(data["createdOn"], data["location"], data["happeningOn"], data["topic"], data["Tags"]) == False:
        return jsonify({"status":400,"error":"One of more fields are empty"}),400
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

    Meetups.append(new_meetup)
    
    return jsonify ({"status":201,"data":[new_meetup]}),201


@mod2.route('/questions', methods=["POST"])
def create_question():
    data = request.get_json()

    last_id = Questions[-1]["id"]
    inc_id = last_id+1

    if vldr.check_empty(data["createdOn"], data["createdBy"], data["meetup"], data["title"], data["body"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
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

    Questions.append(new_question)

    return jsonify({"status": 201, "data": [new_question]}), 201

@mod2.route('/questions/<question_id>/comment',methods=["POST"])
def create_comment(question_id):

    data = request.get_json()

    last_id = Comments[-1]["id"]
    cinc_id = last_id+1

    for entry in Questions:
        if entry["id"] == int(question_id):
            qstn = entry["title"]

    if vldr.check_empty(data["user"], data["responce"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
    id = cinc_id
    question = qstn
    user = data["user"]
    responce = data["responce"]

    new_comment = {
        "id": id,
        "question": question,
        "user": user,
        "responce": responce
    }

    Comments.append(new_comment)

    return jsonify({"status": 201, "data": [new_comment]}), 201

@mod2.route('/meetups/<meetup_id>/rsvp', methods=["POST"])
def rsvp(meetup_id):

    data = request.get_json()

    last_id = Rsvps[-1]["id"]
    inc_id = last_id+1

    if vldr.check_empty(data["user"], data["responce"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
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

    Rsvps.append(new_rsvp)

    for entry in Meetups:
        if entry["id"] == int(meetup_id):
            topic= entry["topic"]
            break
    
    rtrn_obj ={
        "meetup":meetup,
        "topic": topic,
        "responce":responce
    }
    return jsonify({"status": 200, "data": [rtrn_obj]}), 200

@mod2.route('/questions/<question_id>/upvote', methods=["PATCH"])
def upvote(question_id):
    for entry in Questions:
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

@mod2.route('/questions/<question_id>/downvote', methods=["PATCH"])
def downvote(question_id):
    for entry in Questions:
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
