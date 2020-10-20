from db import db
import datetime

class VoteModel(db.Model):
    __tablename__ = "vote"
    _id = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', nullable=False))
    placed_on = db.Column(db.DateTime)

    def __init__(self, voter_id, candidate_id):
        self.voter_id = voter_id
        self.candidate_id = candidate_id
        self.placed_on = datetime.datetime.utcnow()

    def json(self):
        return {
            "_id": self._id,
            "user": self.user,
            "candidate": self.candidate,
            "placed_on": self.placed_on.isoformat(),
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
