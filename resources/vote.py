from flask_restful import Resource, reqparse
import datetime

from models.candidate import CandidateModel

class Vote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("vote_id", type=str)
    parser.add_argument("candidate_id", type=str)
    parser.add_argument("voter_id", type=str)

    def post(self, candidate_name):
        candidate = CandidateModel.find_by_name(name=candidate_name)
        if not candidate:
            candidate = CandidateModel(name=candidate_name)
            candidate.save_to_db()
        candidate.votes = candidate.votes + 1
        return {"candidate name": candidate.name, "votes": candidate.votes}

    def get(self):
        candidates = CandidateModel.query.all()
        json = []
        for candidate in candidates:
            json.append(candidate.json())
        return json