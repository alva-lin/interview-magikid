from . import db
from .enums import Gender
from sqlalchemy.dialects.mysql import ENUM


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'gender': self.gender.value
        }
