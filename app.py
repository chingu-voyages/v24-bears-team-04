from flask import Flask
from flask_restful import Api
from flask_talisman import Talisman
from flask_cors import CORS
from db.db import db
import os

# Import resources here
from resources.vote import Vote
from resources.candidate import Candidate

app = Flask(__name__)
Talisman(app)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///votes-db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

# Replace below with references to resources:
# api.add_resource(Reply, "/api/replies/<board_name>")
# api.add_resource(Thread, "/api/threads/<board_name>")

if __name__ == "__main__":
    app.run(debug=True)