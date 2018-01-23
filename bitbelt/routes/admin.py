from flask_login import login_required, login_user, logout_user, current_user
from bitbelt import app, login_manager

@app.route('/admin')
@login_required
def admin():
    return 'YO ' + current_user.first_name + ' ' + current_user.last_name + '! is_authenticated: ' + str(current_user.is_authenticated)