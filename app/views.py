from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Rags' }
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Post 1'
        },
        {
            'author': {'nickname': 'Amanda'},
            'body': 'Post 2'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
  
