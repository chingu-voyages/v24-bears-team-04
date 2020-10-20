from db import db
import datetime

class VoterModel(db.Model):
    __tablename__ = "voter"
    _id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    votes = db.relationship('Vote', backref='voter')

    def __init__(self, first, last, username, email, password):
        self.created_on = datetime.datetime.utcnow()
        self.first = first
        self.last = last
        self.username = username
        self.email = email
        self.password = password
        
    def json(self):
        return {
            "_id": self._id,
            "first": self.first,
            "last": self.last,
            "username": self.username,
            "email": self.email,
            "created_on": self.created_on.isoformat(),
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
