import ko from 'knockout';

import Client from './client';

export default class ProjectList {
    constructor(clientList) {
        this.clients = ko.observableArray(clientList.map(client => new Client(client)));
    }

    navigate = (client) => {
        window.location.href = '/clients/' + client.id();
    }

    navigateToActiveClientsList = () => {
        window.location.href = '/clients/active/list';
    }

    navigateToInactiveClientsList = () => {
        window.location.href = '/clients/inactive/list';
    }

    navigateToAddClient = () => {
        window.location.href = '/clients/add';
    }
}

