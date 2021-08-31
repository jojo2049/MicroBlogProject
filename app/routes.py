from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jonathan'}
    posts = [
        {
            'author': {'username': 'Dakota'},
            'body': 'Lazy day in Dallas :)'
        }, 
        {
            'author': {'username': 'Appa'},
            'body': "I'm hungry...."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)