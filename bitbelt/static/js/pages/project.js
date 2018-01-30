import ko from 'knockout';
import $ from 'jquery';

import Project from '../models/project';

$(document).ready(function() {
    const project = new Project(projectFromServer);
    ko.applyBindings(project, document.getElementById('project'));
});