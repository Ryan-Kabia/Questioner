from flask import Flask, Blueprint
from app.api.v1.views.meetup_view import mod2
from app.api.v1.views.signup_login_view import mod1

ryan_app = Flask(__name__)

ryan_app.register_blueprint(mod1)
ryan_app.register_blueprint(mod2)
