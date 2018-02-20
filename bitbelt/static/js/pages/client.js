import ko from 'knockout';
import $ from 'jquery';

import Client from '../models/client';

$(document).ready(function() {
    const client = new Client(clientFromServer);
    ko.applyBindings(client, document.getElementById('client'));
});