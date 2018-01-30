import ko from 'knockout';

import User from './user';
import Client from './client';
import DefaultValues from './default-values';
import CabinetOpening from './cabinet-opening';

export default class Project {
    constructor(project) {
        if (!project) {
            throw 'the parameter \'project\' must be provided';
        }

        this.id = ko.observable(project.id);
        this.user = ko.observable(new User(project.user));
        this.client = ko.observable(new Client(project.client));
        this.defaultValues = ko.observable(new DefaultValues(project.defaultValues));
        this.cabinetOpenings = ko.observableArray(project.cabinetOpenings.map(co => new CabinetOpening(co)));
        this.createdOn = ko.observable(project.createdOn);
    }

    navigateLink = () => {
        window.location.href = '/projects/' + this.id() + '/cabinet-openings/create';
    }
}
