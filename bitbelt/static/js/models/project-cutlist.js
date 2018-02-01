import ko from 'knockout';

import Project from './project';
import CutlistItem from './cutlist-item';

export default class ProjectCutlist {
    constructor(project) {
        if (!project) {
            throw 'the parameter \'project\' must be provided';
        }

        this.project = ko.observable(new Project(project));
        this.cutlistItems = ko.observableArray(this.project().cabinetOpenings().map(opening => new CutlistItem(opening, this.project().defaultValues)));
    }

    printPage = () => {
        window.print();
    }
}
