from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from bson import ObjectId

from bitbelt import app
from bitbelt.forms.add_client_form import AddClientForm

from bitbelt.models.client import Client

@app.route('/clients/add', methods=['GET', 'POST'])
@login_required
def add_client():
    form = AddClientForm()
    if(form.validate_on_submit()):
        client = Client()
        client.first_name = form.first_name.data
        client.last_name = form.last_name.data
        client.address = form.address.data
        client.city = form.city.data
        client.state = form.state.data
        client.zip_code = form.zip_code.data
        client.phone = form.phone.data
        client.email = form.email.data

        client.user_id = ObjectId(current_user.user_id)

        client.save()

        current_user.clients.append(client)
        current_user.save()
        return redirect(url_for('index'))
    else:
        return render_template('forms/add-client-form.html', form=form, title='Create Client', user=current_user)


@app.route('/clients/<string:id>/inactivate')
@login_required
def inactivate_client(id):
    if(verify_valid_client(id)):
        client = Client.objects(id=id)
        client.is_active = False
        client.save()


@app.route('/clients/<string:id>/activate')
@login_required
def activate_client(id):
    if(verify_valid_client(id)):
        client = Client.objects(id=id)
        client.is_active = True
        client.save()


def verify_valid_client(id):
    return id in filter(lambda client: str(client.id), current_user.clients)
