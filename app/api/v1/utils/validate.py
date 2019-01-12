import os
from flask import jsonify, request, abort, make_response
from app.api.v1.models.models import *
from datetime import datetime


class Validate():

    def check_empty(self,*args):
       for arg in args:
           if (arg == ""):
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





