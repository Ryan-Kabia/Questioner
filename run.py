import os
from app import create_app

SERECT_KEY = os.urandom(24)
config_name = "development"
ryan_app = create_app(config_name)

if __name__ == "__main__":
    ryan_app.run(debug=True)