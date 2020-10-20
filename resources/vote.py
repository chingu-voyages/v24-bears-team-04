from flask_restful import Resource, reqparse
import datetime

from models.vote import VoteModel

class Vote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("vote_id", type=str)
    parser.add_argument("candidate_id", type=str)
    parser.add_argument("voter_id", type=str)

    def post(self):
        data = Reply.parser.parse_args()
        voter_id = data["voter_id"]
        candidate_id = data["candidate_id"]

        new_vote = VoteModel(
            candidate_id=candidate_id, 
            voter_id=voter_id
        )

        new_vote.save_to_db()
        return new_vote.json(), 201