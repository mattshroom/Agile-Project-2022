# import os

# from flask import Flask
# from config import Config


# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from flask_login import LoginManager

# #from app import routes

# app = Flask(__name__)
# app.config.from_object(Config)


# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# login=LoginManager(app)
# #login.login_view = 'login'

# from app import routes, models

#--MEGA FLASK TUTORIAL--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
