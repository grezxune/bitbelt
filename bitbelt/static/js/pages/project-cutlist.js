import ko from 'knockout';
import $ from 'jquery';

import ProjectCutlist from '../models/project-cutlist';

$(document).ready(function() {
    const projectCutlist = new ProjectCutlist(projectFromServer);
    ko.applyBindings(projectCutlist, document.getElementById('project-cutlist'));
});