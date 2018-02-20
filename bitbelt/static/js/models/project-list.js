import ko from 'knockout';

import Project from './project';

export default class ProjectList {
    constructor(projectList) {
        this.projects = ko.observableArray(projectList.map(project => new Project(project)));
    }

    navigate = (project) => {
        window.location.href = '/projects/' + project.id();
    }

    navigateToFinishedProjectList = () => {
        window.location.href = '/projects/finished-list';
    }

    navigateToActiveProjectList = () => {
        window.location.href = '/projects/list';
    }

    navigateToAddProject = () => {
        window.location.href = '/projects/create';
    }
}

