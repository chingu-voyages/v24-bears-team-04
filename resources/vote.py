from flask_restful import Resource, reqparse
import datetime

from models.candidate import CandidateModel

class Vote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("candidate_name", type=str)

    def post(self):
        data = Vote.parser.parse_args()
        candidate_name = data["candidate_name"]
        candidate = CandidateModel.find_by_name(name=candidate_name)
        if not candidate:
            candidate = CandidateModel(name=candidate_name)
        candidate.votes = candidate.votes + 1
        candidate.save_to_db()
        return {"candidate name": candidate.name, "votes": candidate.votes}

    def get(self):
        candidates = CandidateModel.query.all()
        json = []
        for candidate in candidates:
            json.append(candidate.json())
        return json
