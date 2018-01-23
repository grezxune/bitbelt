from flask import render_template
from flask_login import current_user

from bitbelt import app, login_manager

@app.route('/')
def index():
    return render_template('home.html', title='Home', user=current_user)