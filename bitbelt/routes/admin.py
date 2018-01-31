from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from bitbelt import app, login_manager
from bitbelt.forms.sign_up_form import SignUpForm
from bitbelt.models.user import User

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = SignUpForm()
    if(form.validate_on_submit()):
        existing_user = User.objects(email = form.email.data).first()

        if(current_user.is_authenticated):
            user = current_user
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data

            if(len(form.password.data) > 0):
                user.password = user.hash_password(form.password.data)

            user.save()
            return redirect(url_for('index'))
        else:
            redirect(url_for('index'))
    else:
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        return render_template('admin.html', title='Admin', user=current_user, form=form)
