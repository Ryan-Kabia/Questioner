import os
from app import ryan_app

SERECT_KEY = os.urandom(24)

if __name__ == "__main__":
    ryan_app.run(debug=True)