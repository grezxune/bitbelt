import ko from 'knockout';
import $ from 'jquery';

import CabinetOpening from '../models/cabinet-opening';

$(document).ready(function() {
    console.log(projectIdFromServer);
    console.log(cabinetOpeningFromServer);
    const cabinetOpening = new CabinetOpening(cabinetOpeningFromServer, projectIdFromServer);
    ko.applyBindings(cabinetOpening, document.getElementById('cabinet-opening'));
});