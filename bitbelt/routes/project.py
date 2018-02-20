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
    clients = current_user.clients
    form.client.choices = [(client.id, client.first_name + ' ' + client.last_name) for client in filter(lambda client: client.is_active, clients)]

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
        default_values.middle_gap = form.middle_gap.data
        default_values.tennon_length = form.tennon_length.data
        default_values.center_rail_width = form.center_rail_width.data
        default_values.save()

        project.name = form.name.data
        project.client = form.client.data
        project.wood_species = form.wood_species.data

        project.default_values = default_values
        project.save()

        current_user.projects.append(project)
        current_user.save()
        
        flash('Created project for {0} {1}!'.format(current_user.first_name, current_user.last_name))
        return redirect(url_for('project_home', id=str(project.id)))
    else:
        return render_template('forms/project-form.html', form=form, title='Create Project', user=current_user, is_edit=False)


@app.route('/projects/list')
@login_required
def active_project_list():
    projects = [proj.jsonify() for proj in filter(lambda project: not project.is_finished, current_user.projects)]
    return render_template('active-project-list.html', title='Active Project List', projects=projects, user=current_user)


@app.route('/projects/finished-list')
@login_required
def project_finished_list():
    projects = [proj.jsonify() for proj in filter(lambda project: project.is_finished, current_user.projects)]
    return render_template('finished-project-list.html', title='Finished Project List', projects=projects, user=current_user)


@app.route('/projects/<string:id>')
@login_required
def project_home(id):
    project = next(filter(lambda proj: str(proj.id) == id, current_user.projects), None)
    if(project is not None):
        return render_template('project.html', title='Project Details', project=project.jsonify(), user=current_user)
    else:
        return redirect(url_for('index'))


@app.route('/projects/<string:project_id>/settings', methods=['GET', 'POST'])
@login_required
def project_settings(project_id):
    form = ProjectForm()

    if(verify_valid_project(project_id)):
        project = next(filter(lambda proj: str(proj.id) == project_id, current_user.projects), None)
        clients = current_user.clients
        form.client.choices = [(client.id, client.first_name + ' ' + client.last_name) for client in filter(lambda client: client.is_active or client.id == project.client.id, clients)]

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
            default_values.middle_gap = form.middle_gap.data
            default_values.tennon_length = form.tennon_length.data
            default_values.center_rail_width = form.center_rail_width.data
            default_values.save()

            project.name = form.name.data
            project.client = form.client.data
            project.wood_species = form.wood_species.data

            project.default_values = default_values
            project.save()
            return redirect(url_for('project_home', id=project_id))
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
            form.middle_gap.data = project.default_values.middle_gap
            form.tennon_length.data = project.default_values.tennon_length
            form.center_rail_width.data = project.default_values.center_rail_width

            form.name.data = project.name
            form.client.data = project.client.id
            form.wood_species.data = project.wood_species

            return render_template('forms/project-form.html', form=form, title='Edit Project', user=current_user, is_edit=True)
    else:
        return redirect(url_for('active_project_list'))


@app.route('/projects/<string:id>/cutlist')
@login_required
def project_cutlist(id):
    if(verify_valid_project(id)):
        project = next(filter(lambda proj: str(proj.id) == id, current_user.projects), None)

        if(project is not None):
            return render_template('project-cutlist.html', title='Project Cutlist', user=current_user, project=project.jsonify())
        else:
            return redirect(url_for('active_project_list'))
    else:
        return redirect(url_for('active_project_list'))


@app.route('/projects/<string:id>/finish', methods=['PUT'])
@login_required
def finish_project(id):
    if(verify_valid_project(id)):
        project = next(filter(lambda proj: str(proj.id) == id, current_user.projects), None)
        project.is_finished = True
        project.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/projects/<string:id>/unfinish', methods=['PUT'])
@login_required
def unfinish_project(id):
    if(verify_valid_project(id)):
        project = next(filter(lambda proj: str(proj.id) == id, current_user.projects), None)
        project.is_finished = False
        project.save()
        return json.dumps({'success' : True}), 200, {'ContentType' : 'application/json'} 


def verify_valid_project(project_id):
    project = next(filter(lambda proj: str(proj.id) == project_id, current_user.projects), None)
    return project is not None
