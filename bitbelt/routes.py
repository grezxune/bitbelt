from bitbelt import app, login_manager
from flask import render_template, request, flash, jsonify, abort, redirect, url_for
from bitbelt.models.project import Project
from bitbelt.models.defaultValues import DefaultValues
from bitbelt.models.user import User
from bitbelt.models.client import Client
# from bitbelt.function_decorators.requireJson import require_json
from flask_login import login_required, login_user, logout_user, current_user
from bitbelt.forms import createProject, createUser, createClient, login
from bson import ObjectId


@app.route('/')
def index():
    return render_template('home.html', title='Home')


@app.route('/admin')
@login_required
def admin():
    return 'YO ' + current_user.first_name + ' ' + current_user.last_name + '!'


@app.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    form = createProject.CreateProject()
    print(current_user.user_id)
    clients = Client.objects(user_id = current_user.user_id)
    form.client.choices = [(client.id, client.first_name + ' ' + client.last_name) for client in clients]
    print(form.client.choices)

    if(form.validate_on_submit()):
        project = Project()

        default_values = DefaultValues()
        default_values.left_stile_width = form.left_stile_width.data
        default_values.right_stile_width = form.right_stile_width.data
        default_values.top_rail_width = form.top_rail_width.data
        default_values.bottom_rail_width =  form.bottom_rail_width.data
        default_values.left_overlay = form.left_overlay.data
        default_values.right_overlay = form.right_overlay.data
        default_values.top_overlay = form.top_overlay.data
        default_values.bottom_overlay = form.bottom_overlay.data
        default_values.panel_gap = form.panel_gap.data
        default_values.tennon_length = form.tennon_length.data
        default_values.save()

        # Storing ObjectId instance as user AND client
        project.user = ObjectId(current_user.user_id)
        project.client = form.client.data

        # Storing instance of DefaultValues object as default_values
        project.default_values = default_values
        project.save()
        
        project = Project.objects(id = project.id)[0]
        flash('Created project for {0} {1}!'.format(project.user.first_name, project.user.last_name))
        return redirect(url_for('create_project'))
    else:
        return render_template('forms/create-project.html', form=form, title='Create Project')


@app.route('/project/list')
@login_required
def project_list():
    project_query_set = Project.objects(user = ObjectId(current_user.user_id))
    projects = [{'created_on': project.created_on,
                 'client_first_name': project.client.first_name,
                 'client_last_name': project.client.last_name} for project in project_query_set]
    return jsonify(projects)


@app.route('/project/<string:id>')
def project_home(id):
    project = Project.objects(id = ObjectId(id))
    if(project.count() > 0):
        return jsonify({'client': project[0].client.first_name + ' ' + project[0].client.last_name})
    else:
        return redirect(url_for('index'))


@app.route('/client/create', methods=['GET', 'POST'])
@login_required
def create_client():
    form = createClient.CreateClient()
    if(form.validate_on_submit()):
        client = Client()
        client.first_name = form.first_name.data
        client.last_name = form.last_name.data
        client.address = form.address.data
        client.city = form.city.data
        client.state = form.state.data
        client.zip_code = form.zip_code.data
        client.email = form.email.data

        client.user_id = ObjectId(current_user.user_id)

        client.save()
        return redirect(url_for('index'))
    else:
        return render_template('forms/create-client.html', form=form, title='Create Client')


#### USER ROUTES ####

@login_manager.user_loader
def load_user(user_id):
    print('****************************')
    print('user_id --- ' + str(user_id))
    user_query_set = User.objects(user_id = user_id)

    if(user_query_set.count() > 0):
        return user_query_set[0]
    else:
        return None


@app.route('/user/create', methods=['GET', 'POST'])
def create_user():
    form = createUser.CreateUser()
    if(form.validate_on_submit()):
        existing_users = User.objects(email = form.email.data)
        if(existing_users.count() <= 0):
            user = User()
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data

            # TODO - Hash this password
            user.password = form.password.data

            user.save()

            logout_user()
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('A user with that email already exists')
            return render_template('create-user.html', form=form)
    else:
        return render_template('forms/create-user.html', form=form, title='Create User')


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
            return redirect(url_for('create_user'))
    else:
        if(hasattr(current_user, 'user_id')):
            return redirect(url_for('index'))
        else:
            return render_template('forms/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))