from db.db import db
import datetime

class CandidateModel(db.Model):
    __tablename__ = "candidate"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160))
    votes = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.votes = 0
        
    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "votes": self.votes
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()