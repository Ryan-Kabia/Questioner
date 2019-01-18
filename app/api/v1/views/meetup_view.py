from flask import Flask, jsonify, request, Blueprint
from app.api.v1.models.models import *
from app.api.v1.utils.validate import Validate
from datetime import datetime

#app=Flask(__name__)
bp1 = Blueprint('api2', __name__)

vldr = Validate()

@bp1.route('/meetups/upcoming/')
def all_meetups():
    print(Meetup.get_meetup)
    return jsonify({"status": 200, "data": Meetups}), 200


@bp1.route('/meetups/<meetup_id>')
def specific_meetups(meetup_id):
    for entry in Meetups:
        if entry["id"] == int(meetup_id):
            return jsonify({"status": 200, "data": entry}), 200

    return jsonify ({"status":404,"data":"entry cannot be found"}),404


@bp1.route('/meetups',methods = ["POST"])
def create_meetup():
    data = request.get_json()

    if vldr.check_empty_fields(data["location"], data["happeningOn"], data["topic"], data["Tags"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
    if vldr.check_string(data["location"], data["topic"], data["Tags"]) == False:
        return jsonify({"status": 400, "error": "You can only use a string of letters for location,topic and Tag fields"}), 400
    if vldr.check_date(data["happeningOn"]) == False:
        return jsonify({"status":400, "error":"Bad date format. Use 'dd/mm/yyyy'"}),400
    if vldr.check_valid_date(data["happeningOn"]) == False:
        return jsonify({"status":400, "error":"Invalid Date! Cant be the same as or prior to the current date"}),400


    new_meetup_card = Meetup(data["location"], data["happeningOn"], data["topic"], data["Tags"])

    
    return jsonify ({"status":201,"data":[new_meetup_card.post_meetup()]}),201


@bp1.route('/questions/<meetup_id>', methods=["POST"])
def create_question(meetup_id):
    data = request.get_json()

    if vldr.check_empty_fields(data["createdBy"], data["title"], data["body"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
    if vldr.check_string(data["createdBy"], data["title"]) == False:
        return jsonify({"status": 400, "error": "You can only use a string of letters for createdBy and title fields"}), 400

    for entry in Meetups:
        if entry.get("id") == int(meetup_id):
            meetup = meetup_id

            new_question = Question(data["createdBy"], meetup, data["title"], data["body"])
            return jsonify({"status": 201, "data": [new_question.post_question()]}), 201

    return jsonify({"status": 404, "error": "Specified meetup could not be found"}), 404

@bp1.route('/questions/<question_id>/comment',methods=["POST"])
def create_comment(question_id):

    data = request.get_json()

    if vldr.check_empty_fields(data["user"], data["responce"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
    if vldr.check_string(data["user"]) == False:
        return jsonify({"status": 400, "error": "Only strings of letters allowed in the user field"}), 400
        
    for entry in Questions:
        if entry.get("id") == int(question_id):
            question = entry.get("title")
            new_comment = Comment(data["user"], data["responce"], question)
            return jsonify({"status": 201, "data": [new_comment.post_comment()]}), 201
    
    return jsonify({"status": 404, "error": "Specified question could not be found"}), 404
        
   
@bp1.route('/meetups/<meetup_id>/rsvp', methods=["POST"])
def rsvp(meetup_id):

    data = request.get_json()

    last_id = len(Rsvps)+1
    inc_id = last_id

    if vldr.check_empty_fields(data["user"], data["responce"]) == False:
        return jsonify({"status": 400, "error": "One of more fields are empty"}), 400
    if vldr.check_string(data["user"], data["responce"]) == False:
        return jsonify({"status": 400, "error": "Only string of letters permitted in user and responce fields"}), 400
    if vldr.check_responce(data["responce"]) == False:
        return jsonify({"status":400, "error": "Limit Answers to:Yes, No or Maybe"}), 400

    
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

    rtrn_obj = {
        "meetup": meetup,
        "responce": responce
    }
    for entry in Meetups:
        if entry.get("id") == int(meetup_id):
            rtrn_obj.update(topic = entry.get("topic"))
            return jsonify({"status": 200, "data": [rtrn_obj]}), 200

    return jsonify({"status": 404, "error":"Specified meetup could not be found" }), 404

@bp1.route('/questions/<question_id>/upvote', methods=["PATCH"])
def upvote(question_id):
    for entry in Questions:
        rtrn_obj = {}
        if entry.get("id") == int(question_id):
            meetup = entry.get("meetup")
            rtrn_obj.update(meetup = meetup)
            title = entry.get("title")
            rtrn_obj.update(title = title)
            body = entry.get("body")
            rtrn_obj.update(body = body)
            votes = entry.get("votes")+1
            rtrn_obj.update(votes=votes)

            return jsonify({"status": 201, "data": [rtrn_obj]}), 201

    return jsonify({"status": 404, "error": "Specified question could not be found"}), 404

@bp1.route('/questions/<question_id>/downvote', methods=["PATCH"])
def downvote(question_id):
    for entry in Questions:
        rtrn_obj = {}
        if entry.get("id") == int(question_id):
            meetup = entry.get("meetup")
            rtrn_obj.update(meetup=meetup)
            title = entry.get("title")
            rtrn_obj.update(title=title)
            body = entry.get("body")
            rtrn_obj.update(body=body)
            votes = entry.get("votes")-1
            rtrn_obj.update(votes=votes)

            return jsonify({"status": 201, "data": [rtrn_obj]}), 201

    return jsonify({"status": 404, "error": "Specified question could not be found"}), 404
