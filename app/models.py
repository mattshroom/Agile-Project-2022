from datetime import datetime
from signal import default_int_handler
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'<User {self.username}>'

    # def is_active(self):
    #     """True, as all users are active."""
    #     return True
    # def get_id(self):
    #     """Return the email address to satisfy Flask-Login's requirements."""
    #     return self.email

    # def is_authenticated(self):
    #     """Return True if the user is authenticated."""
    #     return self.authenticated

    # def is_anonymous(self):
    #     """False, as anonymous users aren't supported."""
    #     return False

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

from flask_login import UserMixin

class User(UserMixin, db.Model):
    def is_active(self):
        """True, as all users are active."""
        return True
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
