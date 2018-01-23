from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from bson import ObjectId

from bitbelt import app
from bitbelt.forms.create_cabinet_opening import CreateCabinetOpening

from bitbelt.models.project import Project
from bitbelt.models.cabinet_opening import CabinetOpening


@app.route('/projects/<string:project_id>/cabinet-opening/create', methods=['GET', 'POST'])
@login_required
def create_cabinet_opening(project_id):
    form = CreateCabinetOpening()
    if(ObjectId.is_valid(project_id)):
        project = project_user_id = Project.objects(id=project_id).first()

        if(project is not None):
            project_user_id = project.user.user_id

            if(project_user_id == current_user.user_id):
                project_defaults = Project.objects(id=project_id).first().default_values

                if(form.validate_on_submit()):
                    new_cabinet_opening = CabinetOpening()

                    new_cabinet_opening.left_stile_width = form.left_stile_width.data
                    new_cabinet_opening.right_stile_width = form.right_stile_width.data
                    new_cabinet_opening.top_rail_width = form.top_rail_width.data
                    new_cabinet_opening.bottom_rail_width =  form.bottom_rail_width.data
                    new_cabinet_opening.left_overlay = form.left_overlay.data
                    new_cabinet_opening.right_overlay = form.right_overlay.data
                    new_cabinet_opening.top_overlay = form.top_overlay.data
                    new_cabinet_opening.bottom_overlay = form.bottom_overlay.data
                    new_cabinet_opening.panel_gap = form.panel_gap.data
                    new_cabinet_opening.tennon_length = form.tennon_length.data

                    new_cabinet_opening.number_of_openings = form.number_of_openings.data
                    new_cabinet_opening.number_of_doors = form.number_of_doors.data
                    new_cabinet_opening.opening_width = form.opening_width.data
                    new_cabinet_opening.opening_height = form.opening_height.data
                    new_cabinet_opening.middle_gap = form.middle_gap.data

                    new_cabinet_opening.save()

                    project.cabinet_openings.append(new_cabinet_opening)
                    project.save()

                    return redirect(url_for('project_home', id=project_id))
                else:
                    # Set defaults for new cabinet_opening
                    form.left_stile_width.data = project_defaults.left_stile_width
                    form.right_stile_width.data = project_defaults.right_stile_width
                    form.top_rail_width.data = project_defaults.top_rail_width
                    form.bottom_rail_width.data =  project_defaults.bottom_rail_width
                    form.left_overlay.data = project_defaults.left_overlay
                    form.right_overlay.data = project_defaults.right_overlay
                    form.top_overlay.data = project_defaults.top_overlay
                    form.bottom_overlay.data = project_defaults.bottom_overlay
                    form.panel_gap.data = project_defaults.panel_gap
                    form.tennon_length.data = project_defaults.tennon_length

                    return render_template('forms/create-cabinet-opening.html', title='Create Cabinet Opening', form=form)
            else:
                flash('This project is not available to the current user')
                return render_template('forms/create-cabinet-opening.html', title='Create Cabinet Opening', form=form)
        else:
            flash('This project is not available to the current user')
            return render_template('forms/create-cabinet-opening.html', title='Create Cabinet Opening', form=form)
    else:
        flash('Project ID is invalid')
        return render_template('forms/create-cabinet-opening.html', title='Create Cabinet Opening', form=form)