# Third Party Imports
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

# Bitbelt Imports
from bitbelt.forms import login
from bitbelt import app, login_manager
from bitbelt.forms.sign_up_form import SignUpForm

# Model Imports
from bitbelt.models.user import User
from bitbelt.models.user_settings import UserSettings

login_manager.login_view = 'login_form'

@login_manager.user_loader
def load_user(user_id):
    print('**************************** load_user(user_id)')
    print('user_id --- ' + str(user_id))
    user_query_set = User.objects(user_id = user_id)

    if(user_query_set.count() > 0):
        return user_query_set[0]
    else:
        return None


@app.route('/users/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if(form.validate_on_submit()):
        existing_users = User.objects(email = form.email.data)
        if(existing_users.count() <= 0):
            user = User()
            user_settings = UserSettings()
            user_settings.save()

            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data

            user.password = user.hash_password(form.password.data)
            user.settings = user_settings

            user.save()

            logout_user()
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('A user with that email already exists')
            return render_template('forms/sign-up-form.html', form=form, title='Create User', user=current_user)
    else:
        return render_template('forms/sign-up-form.html', form=form, title='Create User', user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    print('Logging in page about to start')
    form = login.Login()

    if(form.validate_on_submit()):
        user = None
        user_query_set = User.objects(email=form.email.data)

        if(user_query_set.count() > 0):
            user = user_query_set[0]

        if(user is not None and user.check_login(form.email.data, form.password.data)):
            print('user! ' + str(user.first_name))
            if login_user(user):
                print('logged in!')

                next = request.args.get('next')
                # if not is_safe_url(next):
                #     return abort(400)
                return redirect(next or url_for('index'))
            else:
                flash('Login Failed')
        else:
            flash('Invalid email or password')
            return redirect(url_for('login_form'))
    else:
        if(hasattr(current_user, 'user_id')):
            return redirect(url_for('index'))
        else:
            return render_template('forms/login.html', form=form, title='Log In', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))