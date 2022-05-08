from datetime import datetime
from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return f'<User {self.username}>'

class Result(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    guesses = db.Column(db.Integer)
    time = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index =True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    logo_id = db.Column(db.Integer, db.ForeignKey('logo.logo_id'))

    def __repr__(self):
        return f'<Result {self.result_id}>'

class Logo(db.Model):
    logo_id = db.Column(db.Integer, primary_key=True)
    logoname = db.Column(db.String(150))
    logolink = db.Column(db.String(150))

    def __repr__(self):
        return f'<Logo {self.logoname}>'
