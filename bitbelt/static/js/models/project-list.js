import ko from 'knockout';

import Project from './project';

export default class ProjectList {
    constructor(projectList) {
        this.projects = ko.observableArray(projectList.map(project => new Project(project)));
    }

    navigate = (project) => {
        window.location.href = '/projects/' + project.id();
    }
}

