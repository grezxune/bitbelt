# Third Party Imports
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from bson import ObjectId

# Bitbelt Imports
from bitbelt.forms.create_project import CreateProject
from bitbelt import app

# Model Imports
from bitbelt.models.client import Client
from bitbelt.models.project import Project
from bitbelt.models.default_values import DefaultValues

@app.route('/projects/create', methods=['GET', 'POST'])
@login_required
def create_project():
    form = CreateProject()
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


@app.route('/projects/list')
@login_required
def project_list():
    project_query_set = Project.objects(user = ObjectId(current_user.user_id))

    return render_template('project-list.html', title='Project List', projects=project_query_set)


@app.route('/projects/<string:id>')
def project_home(id):
    project_query_set = Project.objects(id = ObjectId(id))
    if(project_query_set.count() > 0):
        return render_template('project.html', title='Project Details', project=project_query_set[0])
    else:
        return redirect(url_for('index'))
