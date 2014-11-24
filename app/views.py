from app import app
from flask import render_template
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kyle'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'User1'},
            'body': 'This is a sample blog post'
        },
        {
            'author': {'nickname': 'User2'},
            'body': 'Sample post2!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
