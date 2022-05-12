from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import app
from app.forms import LoginForm 

from app import db
from flask_login import login_user, login_required, logout_user, current_user

from app.models import User
from werkzeug.urls import url_parse

from app.forms import RegistrationForm 


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

    return render_template("index.html",title="Home",user=user, posts=posts)

@app.route('/button')
def button():
    return render_template("button.html", title="Button!")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#--CRUD ENDPOINTS--

@app.route('/users', methods=['GET'])
def all_users():
    all = User.query.all()
    return all

@app.route('/users', methods=['GET'])
def get_user(id):
    u = User.query.get(id)
    return u.username, u.email

@app.route('users', methods=['PATCH, UPDATE'])
def update_user(id, new_name, new_email):
    u = User.query.get(id)
    if new_name:
        u.username = new_name

    if new_email:
        u.email = new_email
    db.session.commit()
    return 0

@app.route('users', methods=['DELETE'])
def delete_user(id):
    u = User.query.get(id)
    db.session.delete(u)
    db.session.commit()
    return 0



