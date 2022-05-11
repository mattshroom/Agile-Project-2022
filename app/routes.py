from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from app import db

@app.route('/')
@app.route('/index')
@login_required

def index():
    # User login JSON sample
    user = {'username':'Matt'}

    # Post JSON sample
    posts = [
        {
            'author':{'username':'Matt'},
            'body':'Test Body'
        },
        {
            'author':{'username':'Matt'},
            'body':'Test Body 2'
        }
    ]

    return render_template("index.html", title='Home Page', posts=posts)

@app.route('/button')
def button():
    return render_template("button.html", title="Button!")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(url_for('index'))
    
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     form = LoginForm()
    
#     if form.validate_on_submit():
        
#         flash('login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
    
#     return render_template('login.html', title='sign in', form=form)

# @login_manager.user_loader
# def user_loader(user):
#     """Given *user_id*, return the associated User object.

#     :param unicode user_id: user_id (email) user to retrieve

#     """
#     return User.query.get(user.id)


# def login():
#     """For GET requests, display the login form. 
#     For POSTS, login the current user by processing the form.

#     """
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.get(form.email.data)
#         if user:
#             if bcrypt.check_password_hash(user.password, form.password.data):
#                 user.authenticated = True
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user, remember=True)
#                 return redirect(url_for("bull.reports"))
#     return render_template("login.html", form=form)

# @app.route("/logout", methods=["GET"])
# @login_required
# def logout():
#     """Logout the current user."""
#     user = current_user
#     user.authenticated = False
#     db.session.add(user)
#     db.session.commit()
#     logout_user()
#     return render_template("logout.html")