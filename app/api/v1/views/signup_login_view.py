from flask import Flask, jsonify, request, Blueprint
from app.api.v1.models.models import Meetups, Questions, Rsvps, Users
from app.api.v1.utils.validate  import Validate

mod1 = Blueprint('api', __name__)
vldr = Validate()

@mod1.route('/signup', methods=["POST"])
def create_user():
    data = request.get_json()

    last_id = Users[-1]["id"]
    uinc_id = last_id+1


    if vldr.check_empty(data["name"], data["email"], data["username"], data["password"]) == False:
        return jsonify({"Message": "empty field"})

    if vldr.check_valid_email(data["email"]) == False:
        return jsonify({"Message": "invalid email"})

    if vldr.check_registered_email(data["email"]) == False:
        return jsonify({"Message": "Email already in use"})

    if vldr.check_registered_username(data["username"]) == False:
        return jsonify({"Message": "username already taken"})

    if vldr.check_password(data["password"]) == False:
        return jsonify({"Message": "must be atleast 8 xters with atleast an upper,lower and number"})

    if vldr.check_date(data["registered"]) == False:
        return jsonify({"Message": "Bad date format"})
    elif vldr.check_valid_date(data["registered"]) == False:
        return jsonify({"Message": "date can not be earlier that current date"})

    id = uinc_id
    name = data["name"]
    email = data["email"]
    username = data["username"]
    password = data["password"]
    registered = data["registered"]

    user = {
        "id": id,
        "name": name,
        "email": email,
        "username": username,
        "password": password,
        "registered": registered,
        "isAdmin":False
    }

    Users.append(user)

    return jsonify({"status": 200, "data": [user]}), 200


@mod1.route('/signin', methods=["POST"])
def signin_user():
    data = request.get_json()

    if vldr.check_empty(data["username"], data["password"]) == False:
        return jsonify({"Message": "empty field"})

    if vldr.check_registered_username(data["username"]) != False:
        return jsonify({"Message": "invalid username"})

    if vldr.check_password(data["password"]) == False:
        return jsonify({"Message": "must be atleast 8 xters with atleast an upper,lower and number"})

    if vldr.check_registered_password(data["username"], data["password"]) != False:
        return jsonify({"Message": "wrong password"})


    return jsonify({"status": 201, "data": ["{} logged in successfully".format(data["username"])]}), 201
    


   


