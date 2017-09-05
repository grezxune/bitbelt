from bitbelt import app, login_manager
from flask import render_template, request, flash, jsonify, abort, redirect, url_for
from bitbelt.models.project import Project
from bitbelt.models.defaultValues import DefaultValues
from bitbelt.models.user import User
from bitbelt.function_decorators.requireJson import require_json
from flask_login import login_required, login_user, logout_user, current_user

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


@app.route('/create-project', methods=['POST'])
@require_json
def create_project():
    print(request.json)
    if(request.json['project'] is not None and
       request.json['project']['default_values'] is not None):
        project = request.json['project']
        default_values = project['default_values']
        return jsonify({'message': 'Successfully created new project!'})


@login_manager.user_loader
def load_user(user_id):
    print('****************************')
    print('user_id --- ' + str(user_id))
    return User.objects(user_id=user_id)[0]


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
@require_json
def login():
    print('got to login...')
    if(request.json is not None and
       request.json['login'] is not None and
       request.json['login']['email'] is not None and
       request.json['login']['password'] is not None):

        print('here1')
        user_query_set = User.objects(email=request.json['login']['email'])

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

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))