from db import db
import datetime

class CandidateModel(db.Model):
    __tablename__ = "candidate"
    _id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))
    votes = db.relationship('Vote', backref='candidate')

    def __init__(first, last):
        self.first = first
        self.last = last
        
    def json(self):
        return {
            "_id": self._id,
            "first": self.first,
            "last": self.last,
            "votes": self.votes.count()
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
