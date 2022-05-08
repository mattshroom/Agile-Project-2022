from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')

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
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        flash('login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='sign in', form=form)