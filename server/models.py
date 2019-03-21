from datetime import datetime
from clear_my_record_backend.server import dbs
from enum import Enum


class Qualifying_Question(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    question = dbs.Column(dbs.Text)
    help_text = dbs.Column(dbs.Text)
    disqualifying_answer = dbs.Column(dbs.String(250))


class Qualifying_Answer(dbs.Model):
    # First Integer ID is set as autoincrement in SQLAlchemy
    id = dbs.Column(dbs.Integer, primary_key=True)
    user_session = dbs.Column(dbs.String(250), index=True, unique=False)
    question_id = dbs.Column(dbs.String(250))
    answer = dbs.Column(dbs.Text)
    qualifying_answer = dbs.Column(dbs.String(250))
    question_version_number = dbs.Column(dbs.Float(asdecimal=True))
    timestamp = dbs.Column(dbs.DateTime, index=True)
    answerer_id = dbs.Column(dbs.Integer, dbs.ForeignKey("user.id"))

    def __init__(self, *data, **kwargs):
        super(Qualifying_Answer, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])


class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    username = dbs.Column(dbs.String(32), index=True, unique=True)
    email = dbs.Column(dbs.String(120), index=True, unique=True)
    pw_hash = dbs.Column(dbs.String(128))
    submissions = dbs.relationship(
        "Qualifying_Answer", backref="author", lazy="dynamic")

    def __init__(self, *data, **kwargs):
        super(User, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __repr__(self):
        return "<USER: {}".format(self.username)

class Client(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    convictions = dbs.relationship()

class Conviction(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    # client_id
    case_number = dbs.Column(dbs.String)
    court = dbs.Column(dbs.String)
    jurisdiction = dbs.Column(dbs.String)
    judge = dbs.Column(dbs.String)
    record_name = dbs.Column(dbs.String)
    release_status = dbs.Column(dbs.String)
    release_date = dbs.Column(dbs.Date)
    charges = dbs.relationship()

class Charge(dbs.Model):
    charge_types = Enum('CHARGE', 'FELONY MISDEMEANOR')
    class_types = Enum('CLASS', 'A B C D E UNDEFINED')

    id = dbs.Column(dbs.Integer, primary_key=True)
    conviction = dbs.relationship()
    charge = dbs.Column(dbs.String)
    sentence = dbs.Column(dbs.String)
    charge_type = dbs.Column(dbs.Enum(charge_types))
    class_type = dbs.Column(dbs.Enum(class_types))
