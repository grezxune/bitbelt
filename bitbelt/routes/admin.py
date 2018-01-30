from flask import render_template
from flask_login import login_required, login_user, logout_user, current_user
from bitbelt import app, login_manager

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', title='Admin', user=current_user)