from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/base')

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