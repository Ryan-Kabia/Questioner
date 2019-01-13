import os
from flask import jsonify, request, abort, make_response
from app.api.v1.models.models import Meetups,Questions,Rsvps,Users
from datetime import datetime
import re


class Validate():

    def check_empty(self,*args):
       for arg in args:
           if arg == "":
            return False

    def check_responce(self, *args):
       for arg in args:
           if (arg not in ["yes","no","maybe"]):
            return False
    
    def check_date(self,*args):
            for arg in args:
                try:
                    datetime.strptime(arg, "%d/%m/%Y")
                except ValueError:
                    return False
              

    def check_valid_date(self, *args):
        now = datetime.now()
        for arg in args:
            if (arg < now.strftime("%d/%m/%Y")):
                return False

    def check_valid_email(self, email):
        vemail = re.compile(r'(\w+[.|\w])*@(\w+[.])*\w+')

        if not vemail.match(email):
            return False

    def check_registered_email(self, email):
        for user in Users:
            if email == user['email']:
                return False

    def check_registered_username(self, username):
        for user in Users:
            if username == user['username']:
                return False

    def check_registered_password(self, username,password):
        for user in Users:
            if username == user['username']:
                if password == user['password']:
                    return False

    def check_password(self, password):

        if (len(password) < 8) or (len(password) > 20):
            return False
        elif not re.search("[A-Z]", password) and not re.search("[a-z]", password) and not re.search("[0-9]", password):
            return False
        



