from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from bson import ObjectId
import json

from bitbelt import app
from bitbelt.forms.add_client_form import AddClientForm

from bitbelt.models.client import Client

@app.route('/clients/add', methods=['GET', 'POST'])
@login_required
def add_client():
    form = AddClientForm()
    client = Client()
    if(form.validate_on_submit()):
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
        return redirect(url_for('active_clients_list'))
    else:
        return render_template('forms/client-form.html', form=form, title='Add Client', user=current_user, is_edit=False, client=client.jsonify())


@app.route('/clients/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_client(id):
    if(verify_valid_client(id)):
        print('Verified')
        client = next(filter(lambda client: str(client.id) == id, current_user.clients), None)

        if(client is not None):
            form = AddClientForm()
            if(form.validate_on_submit()):
                client.first_name = form.first_name.data
                client.last_name = form.last_name.data
                client.address = form.address.data
                client.city = form.city.data
                client.state = form.state.data
                client.zip_code = form.zip_code.data
                client.phone = form.phone.data
                client.email = form.email.data
                client.save()
                return render_template('forms/client-form.html', form=form, title='Edit Client', user=current_user, is_edit=True, client=client.jsonify())
            else:
                form.first_name.data = client.first_name
                form.last_name.data = client.last_name
                form.address.data = client.address
                form.city.data = client.city
                form.state.data = client.state
                form.zip_code.data = client.zip_code
                form.phone.data = client.phone
                form.email.data = client.email
                return render_template('forms/client-form.html', form=form, title='Edit Client', user=current_user, is_edit=True, client=client.jsonify())
        else:
            print('client was None')
            return redirect(url_for('active_clients_list'))
    else:
        print('Not verified')
        return redirect(url_for('active_clients_list'))


@app.route('/clients/active/list')
@login_required
def active_clients_list():
    clients = [client.jsonify() for client in filter(lambda client: client.is_active, current_user.clients)]
    return render_template('active-clients-list.html', title='Active Client List', user=current_user, clients=clients)


@app.route('/clients/inactive/list')
@login_required
def inactive_clients_list():
    clients = [client.jsonify() for client in filter(lambda client: not client.is_active, current_user.clients)]
    return render_template('inactive-clients-list.html', title='Inactive Client List', user=current_user, clients=clients)


@app.route('/clients/<string:id>/deactivate', methods=['PUT'])
@login_required
def deactivate_client(id):
    if(verify_valid_client(id)):
        client = next(filter(lambda client: str(client.id) == id, current_user.clients))
        client.is_active = False
        client.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/clients/<string:id>/activate', methods=['PUT'])
@login_required
def activate_client(id):
    if(verify_valid_client(id)):
        client = next(filter(lambda client: str(client.id) == id, current_user.clients))
        client.is_active = True
        client.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


def verify_valid_client(id):
    return id in [str(client.id) for client in current_user.clients]
