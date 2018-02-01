# Third Party Imports
import json
from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from bson import ObjectId

# Bitbelt Imports
from bitbelt.forms.project_form import ProjectForm
from bitbelt import app

# Model Imports
from bitbelt.models.client import Client
from bitbelt.models.project import Project
from bitbelt.models.default_values import DefaultValues

@app.route('/projects/create', methods=['GET', 'POST'])
@login_required
def create_project():
    form = ProjectForm()
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
        default_values.center_rail_width = form.center_rail_width.data
        default_values.save()

        project.user = ObjectId(current_user.user_id)
        project.name = form.name.data
        project.client = form.client.data
        project.wood_species = form.wood_species.data

        project.default_values = default_values
        project.save()
        
        project = Project.objects(id = project.id).first()
        flash('Created project for {0} {1}!'.format(project.user.first_name, project.user.last_name))
        return redirect(url_for('project_home', id=project.id))
    else:
        print('Form not validated')
        return render_template('forms/project-form.html', form=form, title='Create Project', user=current_user)


@app.route('/projects/list')
@login_required
def project_list():
    project_query_set = Project.objects(user = ObjectId(current_user.user_id))
    projects = [proj.jsonify() for proj in project_query_set]
    return render_template('project-list.html', title='Project List', projects=projects, user=current_user)


@app.route('/projects/<string:id>')
@login_required
def project_home(id):
    project = Project.objects(id = ObjectId(id)).first()
    if(project is not None):
        return render_template('project.html', title='Project Details', project=project.jsonify(), user=current_user)
    else:
        return redirect(url_for('index'))


@app.route('/projects/<string:project_id>/settings', methods=['GET', 'POST'])
@login_required
def project_settings(project_id):
    form = ProjectForm()

    if(verify_valid_project(project_id)):
        project = Project.objects(id=project_id).first()
        clients = Client.objects(user_id = current_user.user_id)
        form.client.choices = [(client.id, client.first_name + ' ' + client.last_name) for client in clients]

        if(form.validate_on_submit()):
            default_values = project.default_values

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
            default_values.center_rail_width = form.center_rail_width.data
            default_values.save()

            project.name = form.name.data
            project.client = form.client.data
            project.wood_species = form.wood_species.data

            project.default_values = default_values
            project.save()
            flash('Successfully updated project!')
            return redirect(url_for('project_settings', project_id=project_id))
        else:
            form.left_stile_width.data = project.default_values.left_stile_width
            form.right_stile_width.data = project.default_values.right_stile_width
            form.top_rail_width.data = project.default_values.top_rail_width
            form.bottom_rail_width.data = project.default_values.bottom_rail_width
            form.left_overlay.data = project.default_values.left_overlay
            form.right_overlay.data = project.default_values.right_overlay
            form.top_overlay.data = project.default_values.top_overlay
            form.bottom_overlay.data = project.default_values.bottom_overlay
            form.panel_gap.data = project.default_values.panel_gap
            form.tennon_length.data = project.default_values.tennon_length
            form.center_rail_width.data = project.default_values.center_rail_width

            form.name.data = project.name
            form.client.data = project.client.id
            form.wood_species.data = project.wood_species

            return render_template('forms/project-form.html', form=form, title='Edit Project', user=current_user)
    else:
        flash('Project does not belong to current user')
        return redirect(url_for('project_list'))


@app.route('/projects/<string:id>/cutlist')
@login_required
def project_cutlist(id):
    project = Project.objects(id=id).first()

    if(project is not None):
        return render_template('project-cutlist.html', title='Project Cutlist', user=current_user, project=project.jsonify())
    else:
        return redirect(url_for('project_list'))


def verify_valid_project(project_id):
    valid_project = False

    if(ObjectId.is_valid(project_id)):
        project = Project.objects(id=project_id).first()

        if(project is not None and project.user.user_id == current_user.user_id):
            valid_project = True
    
    return valid_project