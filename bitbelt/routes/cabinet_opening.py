from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from bson import ObjectId

from bitbelt import app
from bitbelt.forms.create_cabinet_opening import CreateCabinetOpening

from bitbelt.models.project import Project
from bitbelt.models.cabinet_opening import CabinetOpening

from bitbelt.routes.project import verify_valid_project


@app.route('/projects/<string:project_id>/cabinet-openings/create', methods=['GET', 'POST'])
@login_required
def create_cabinet_opening(project_id):
    form = CreateCabinetOpening()
    if(verify_valid_project(project_id)):
        project = Project.objects(id=project_id).first()
        project_defaults = project.default_values

        new_cabinet_opening = CabinetOpening()

        if(form.validate_on_submit()):
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
            new_cabinet_opening.center_rail_width = form.center_rail_width.data
            new_cabinet_opening.rough_sawn_overestimate = current_user.settings.rough_sawn_overestimate

            new_cabinet_opening.number_of_openings = form.number_of_openings.data
            new_cabinet_opening.number_of_doors = form.number_of_doors.data
            new_cabinet_opening.number_of_panels_per_door = form.number_of_panels_per_door.data
            new_cabinet_opening.opening_width = form.opening_width.data
            new_cabinet_opening.opening_height = form.opening_height.data
            new_cabinet_opening.middle_gap = form.middle_gap.data
            new_cabinet_opening.center_rail_horizontal = form.center_rail_horizontal.data

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
            form.center_rail_width.data = project_defaults.center_rail_width

            return render_template('forms/cabinet-opening-form.html', title='Create Cabinet Opening', form=form, cabinet_opening=new_cabinet_opening.jsonify(), user=current_user)
    else:
        return redirect(url_for('project_list'))


@app.route('/projects/<string:project_id>/cabinet-openings/<string:cabinet_opening_id>', methods=['GET', 'POST'])
@login_required
def cabinet_opening_details(project_id, cabinet_opening_id):
    print('in get, put')
    if(verify_valid_project(project_id) and verify_valid_cabinet_opening(project_id, cabinet_opening_id)):
        cabinet_openings = Project.objects(id=project_id).first().cabinet_openings
        cabinet_opening = next(filter(lambda x: str(x.id) == cabinet_opening_id, cabinet_openings), None)

        if(cabinet_opening is not None):
            form = CreateCabinetOpening()

            if(form.validate_on_submit()):
                cabinet_opening.number_of_openings = form.number_of_openings.data
                cabinet_opening.number_of_doors = form.number_of_doors.data
                cabinet_opening.number_of_panels_per_door = form.number_of_panels_per_door.data
                cabinet_opening.opening_width = form.opening_width.data
                cabinet_opening.opening_height = form.opening_height.data
                cabinet_opening.middle_gap = form.middle_gap.data
                cabinet_opening.center_rail_horizontal = form.center_rail_horizontal.data

                # Set by default values
                cabinet_opening.left_stile_width = form.left_stile_width.data
                cabinet_opening.right_stile_width = form.right_stile_width.data
                cabinet_opening.top_rail_width = form.top_rail_width.data
                cabinet_opening.bottom_rail_width = form.bottom_rail_width.data
                cabinet_opening.left_overlay = form.left_overlay.data
                cabinet_opening.right_overlay = form.right_overlay.data
                cabinet_opening.top_overlay = form.top_overlay.data
                cabinet_opening.bottom_overlay = form.bottom_overlay.data
                cabinet_opening.panel_gap = form.panel_gap.data
                cabinet_opening.tennon_length = form.tennon_length.data
                cabinet_opening.center_rail_width = form.center_rail_width.data
                cabinet_opening.rough_sawn_overestimate = current_user.settings.rough_sawn_overestimate

                cabinet_opening.save()

                flash('Successfully saved cabinet opening')
                return redirect(url_for('project_home', id=project_id))
            else:
                form.number_of_openings.data = cabinet_opening.number_of_openings
                form.number_of_doors.data = cabinet_opening.number_of_doors
                form.number_of_panels_per_door.data = cabinet_opening.number_of_panels_per_door
                form.opening_width.data = cabinet_opening.opening_width
                form.opening_height.data = cabinet_opening.opening_height
                form.middle_gap.data = cabinet_opening.middle_gap
                form.center_rail_horizontal.data = cabinet_opening.center_rail_horizontal

                # Set by default values
                form.left_stile_width.data = cabinet_opening.left_stile_width
                form.right_stile_width.data = cabinet_opening.right_stile_width
                form.top_rail_width.data = cabinet_opening.top_rail_width
                form.bottom_rail_width.data = cabinet_opening.bottom_rail_width
                form.left_overlay.data = cabinet_opening.left_overlay
                form.right_overlay.data = cabinet_opening.right_overlay
                form.top_overlay.data = cabinet_opening.top_overlay
                form.bottom_overlay.data = cabinet_opening.bottom_overlay
                form.panel_gap.data = cabinet_opening.panel_gap
                form.tennon_length.data = cabinet_opening.tennon_length
                form.center_rail_width.data = cabinet_opening.center_rail_width

                return render_template('forms/cabinet-opening-form.html', title='Edit Cabinet Opening', form=form, cabinet_opening=cabinet_opening.jsonify(), user=current_user)
        else:
            return redirect(url_for('project_list'))

    return redirect(url_for('project_list'))


@app.route('/projects/<string:project_id>/cabinet-openings/<string:cabinet_opening_id>', methods=['DELETE'])
@login_required
def delete_cabinet_opening(project_id, cabinet_opening_id):
    print('In delete')
    if(verify_valid_project(project_id) and verify_valid_cabinet_opening(project_id, cabinet_opening_id)):
        project = Project.objects(id=project_id).first()
        cabinet_opening = next(filter(lambda x: str(x.id) == cabinet_opening_id, project.cabinet_openings), None)

        if(cabinet_opening is not None):
            project.cabinet_openings.remove(cabinet_opening)
            project.save()
            cabinet_opening.delete()
            flash('Successfully removed cabinet opening')
        else:
            flash('Could not find cabinet opening')
    else:
        flash('Could not find project or cabinet opening')

    return redirect(url_for('project_list'))




def verify_valid_cabinet_opening(project_id, cabinet_opening_id):
    valid_cabinet_opening = False
    project = Project.objects(id=project_id).first()

    if(project is not None):
        cabinet_openings = project.cabinet_openings
        valid_cabinet_openings = list(filter(lambda opening: str(opening.id) == cabinet_opening_id, cabinet_openings))

        if(len(valid_cabinet_openings) > 0):
            valid_cabinet_opening = True
    
    return valid_cabinet_opening
