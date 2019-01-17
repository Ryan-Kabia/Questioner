import os
from flask import Flask, Blueprint
from instance.config import app_config
from app.api.v1.views.meetup_view import bp1



def create_app(config_name):

    ryan_app = Flask(__name__, instance_relative_config=True)
    ryan_app.secret_key = os.getenv("SECRET")
    ryan_app.config.from_object(app_config[config_name])

    ryan_app.register_blueprint(bp1)

    return ryan_app
