from bitbelt import app, login_manager
from flask import render_template, request, flash, jsonify, abort, redirect, url_for
from bitbelt.models.project import Project
from bitbelt.models.defaultValues import DefaultValues
from bitbelt.models.user import User
from bitbelt.models.client import Client
# from bitbelt.function_decorators.requireJson import require_json
from flask_login import login_required, login_user, logout_user, current_user
from bitbelt.forms import createProject, createUser, createClient, login

@app.route('/')
def index():
    # default_values = DefaultValues()
    # default_values.save()
    # proj = Project(default_values)
    # proj.save()

    # for test in Project.objects:
    #     print(test.default_values.left_overlay)

    # user = current_user
    # print('current user! ' + str(user.first_name) + ' IS FUCKING AWESOME!')
    # flash('testing flash!')
    return render_template('home.html', Title='Home')


@app.route('/admin')
@login_required
def admin():
    return 'YO!'


@app.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    form = createProject.CreateProject()
    print(request.json)
    if(form.validate_on_submit()):
        return redirect(url_for('index'))
    else:
        clients = Client.objects()
        form.client.choices = [(client.id, client.first_name + ' ' + client.last_name) for client in clients]
        return render_template('create-project.html', form=form)
    # if(request.json['project'] is not None and
    #    request.json['project']['default_values'] is not None):
    #     project = request.json['project']
    #     default_values = project['default_values']
    #     return jsonify({'message': 'Successfully created new project!'})


@app.route('/client/create', methods=['GET', 'POST'])
@login_required
def create_client():
    form = createClient.CreateClient()
    if(form.validate_on_submit()):
        print('client validated')
        client = Client()
        client.first_name = form.first_name.data
        client.last_name = form.last_name.data
        client.address = form.address.data
        client.city = form.city.data
        client.state = form.state.data
        client.zip_code = form.zip_code.data
        client.email = form.email.data

        client.save()
        # return 'Successfully created client {0} {1}!'.format(client.first_name, client.last_name)
        print('created client!')
        return redirect(url_for('index'))
    else:
        print('client NOT validated')
        return render_template('create-client.html', form=form)


#### USER ROUTES ####

@login_manager.user_loader
def load_user(user_id):
    print('****************************')
    print('user_id --- ' + str(user_id))
    return User.objects(user_id=user_id)[0]


@app.route('/user/create', methods=['GET', 'POST'])
def create_user_form():
    form = createUser.CreateUser()
    if(form.validate_on_submit()):
        print('passed!')
        print(form.middle_name.data == '')
        print(str.join(', ', [form.first_name.data, form.middle_name.data, form.last_name.data, form.email.data, form.password.data]))
        return redirect(url_for('index'))
    else:
        print('failed!')
        print(form.password.data)
        return render_template('create-user.html', form=form)


@app.route('/create-user', methods=['POST'])
def create_user():
    user_info = request.json['user']
    if(user_info is not None):
        if(User.objects(email=user_info['email']).count() <= 0):
            user = User(user_info['first_name'],
                        user_info['last_name'],
                        user_info['middle_name'],
                        user_info['email'],
                        user_info['password'])
            user.save()
            return 'successfully created user for {0} {1} {2}'.format(user_info['first_name'], user_info['middle_name'], user_info['last_name'])

    return 'Something went wrong...'


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    form = login.Login()

    if(form.validate_on_submit()):
        user_query_set = User.objects(email=form.email.data)

        if(user_query_set.count() > 0):
            user = user_query_set[0]
            print('user! ' + str(user.first_name))
            login_user(user)
            print('logged in!')

            next = request.args.get('next')
            # if not is_safe_url(next):
            #     return abort(400)
            print('returnin')
            return redirect(next or url_for('index'))
    else:
        if(hasattr(current_user, 'user_id')):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))