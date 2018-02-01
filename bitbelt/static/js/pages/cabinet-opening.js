import ko from 'knockout';
import $ from 'jquery';

import CabinetOpening from '../models/cabinet-opening';

$(document).ready(function() {
    const cabinetOpening = new CabinetOpening(cabinetOpeningFromServer);
    ko.applyBindings(cabinetOpening, document.getElementById('cabinet-opening'));
});