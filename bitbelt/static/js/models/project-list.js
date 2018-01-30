import ko from 'knockout';

import Project from './project';

export default class ProjectList {
    constructor(projectList) {
        const projectsListed = projectList.map(project => new Project(project));
        this.projects = ko.observableArray(projectList.map(project => new Project(project)));
    }

    navigate = (project) => {
        window.location.href = '/projects/' + project.id();
    }
}

