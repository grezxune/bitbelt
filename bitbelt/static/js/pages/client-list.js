import ko from 'knockout';
import $ from 'jquery';

import ClientList from '../models/client-list';

$(document).ready(function() {
    const clientList = new ClientList(clientsFromServer);
    ko.applyBindings(clientList, document.getElementById('client-list'));
});