from flask_restful import Resource, reqparse
import datetime

from models.candidate import CandidateModel

class Candidate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("first", type=str)
    parser.add_argument("last", type=str)
    parser.add_argument("candidate_id", type=str)

    def get(self, board_name):
        candidate_id = Reply.parser.parse_args()["candidate_id"]
        candidate = CandidateModel.find_by_id(_id=candidate_id)
        return candidate.json()