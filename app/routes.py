from flask import render_template, url_for, flash, redirect, request, Blueprint, session

from app import app
from app.forms import LoginForm, ResultsForm, RegistrationForm 

from app import db
from flask_login import login_user, login_required, logout_user, current_user

from app.models import User, Result
from werkzeug.urls import url_parse
from datetime import datetime


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
            'body':'Welcome to Blurgo!'
        },
        {
            'author':{'username':'Nic'},
            'body':'Try to guess the company logo as it unblurs!'
        },
        {
            'author':{'username':'Cameron'},
            'body':'There is a new Blurgo every day!'
        },
        {
            'author':{'username':'Lachy'},
            'body':'Compete with your friends to get the best score!'
        },
        {
            'author':{'username':'Matt'},
            'body':'Click on the "Blurgo" at the top to play!'
        }
    ]

    return render_template("index.html",title="Home",user=user, posts=posts)


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

@app.route('/button', methods=['GET', 'POST'])
@login_required
def button():
    
    resultform = ResultsForm() 

    user = User.query.get(current_user.id)
    print("user is: ", user.id)

    scores = db.session.query(Result).filter(user.id==current_user.id).all()
    total = 0    
    for s in scores:
        total += s.score
    current_user.average = round(total/len(scores))

    if resultform.validate_on_submit():
        result = Result(score=resultform.score.data, guesses=resultform.guesses.data, time=resultform.time.data, user_id=current_user.id,logo_id=resultform.logo.data)
        db.session.add(result)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('button.html', title='Button!', form=resultform)