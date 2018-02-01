from flask import render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from bitbelt import app, login_manager
from bitbelt.forms.user_settings_form import UserSettingsForm
from bitbelt.models.user import User
from bitbelt.models.user_settings import UserSettings

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = UserSettingsForm()

    if(current_user.settings is None):
        print('Creating new settings for user')
        new_settings = UserSettings()
        new_settings.save()
        current_user.settings = new_settings
        current_user.save()

    if(form.validate_on_submit()):
        user = current_user
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.settings.rough_sawn_overestimate = form.rough_sawn_overestimate.data

        user.save(cascade=True)
        flash('Successfully saved user!')
        return render_template('admin.html', title='Admin', user=current_user, form=form)
    else:
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.rough_sawn_overestimate.data = current_user.settings.rough_sawn_overestimate
        return render_template('admin.html', title='Admin', user=current_user, form=form)
