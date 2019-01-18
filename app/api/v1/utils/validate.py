import os
from flask import jsonify, request, abort, make_response
from app.api.v1.models.models import Meetups,Questions,Rsvps,Users
from datetime import datetime
import re


class Validate():

    def check_empty_fields(self,*args):
       for arg in args:
           if not arg.split():
            return False

    def check_string(self, *args):
       for arg in args:
           arg = arg.split()
           if not arg[0].isalpha():
            return False

    def check_responce(self, *args):
       for arg in args:
           if arg.lower() not in ["yes","no","maybe"]:
            return False
    
    def check_date(self,*args):
            for arg in args:
                try:
                    datetime.strptime(arg, "%d/%m/%Y")
                except ValueError:
                    return False
              

    def check_valid_date(self, *args):
        current_date = datetime.utcnow()
        current_date.strftime("%d/%m/%Y")
        for arg in args:
            arg = datetime.strptime(arg, "%d/%m/%Y")
            if (arg < current_date):
                return False

    
        



