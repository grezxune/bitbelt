import ko from 'knockout';
import $ from 'jquery';

import ProjectList from '../models/project-list';

$(document).ready(function() {
    const projectList = new ProjectList(projectsFromServer);
    ko.applyBindings(projectList, document.getElementById('project-list'));

    // $(document).on('click', '.project', function(e) {
    //     window.location.href = '/projects/' + e.currentTarget.id;
    // });
});