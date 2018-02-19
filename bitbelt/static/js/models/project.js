import ko from 'knockout';
import $ from 'jquery';

import User from './user';
import Client from './client';
import DefaultValues from './default-values';
import CabinetOpening from './cabinet-opening';

import { formatMomentDate, capitalizeFirstLetterOfEachWordAndLowercaseAllOthers } from '../utils';

export default class Project {
    constructor(project) {
        if (!project) {
            throw 'the parameter \'project\' must be provided';
        }

        this.dateCreated = ko.observable(formatMomentDate(project.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(project.lastModified));

        this.id = ko.observable(project.id);
        this.name = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(project.name));
        this.client = ko.observable(new Client(project.client));
        this.defaultValues = ko.observable(new DefaultValues(project.defaultValues));
        this.cabinetOpenings = ko.observableArray(project.cabinetOpenings.map(co => new CabinetOpening(co)));
        this.woodSpecies = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(project.woodSpecies));
        this.isFinished = ko.observable(project.isFinished);

        this.projectPageTitle = ko.computed(() => {
            return 'Viewing project \"' + this.name() + '\"';
        });

        this.numberOfOpeningsInProject = ko.computed(() => {
            const numberOfOpeningsArray = this.cabinetOpenings().map(opening => opening.numberOfOpenings());
            const reducedNumberOfOpenings = numberOfOpeningsArray.reduce((a, b) => a + b, 0);
            return reducedNumberOfOpenings;
        });

        this.totalNumberOfCenterRails = ko.computed(() => {
            return this.cabinetOpenings().reduce((accumulated, current) => accumulated + current.totalNumberOfCenterRails(), 0);
        });
    }

    navigateToAddOpening = () => {
        window.location.href = '/projects/' + this.id() + '/cabinet-openings/create';
    }

    navigateToCutlist = () => {
        window.location.href = '/projects/' + this.id() + '/cutlist';
    }

    navigateToSettings = () => {
        window.location.href = '/projects/' + this.id() + '/settings';
    }

    navigateToCabinetOpening = (opening) => {
        window.location.href = '/projects/' + this.id() + '/cabinet-openings/' + opening.id();
    }

    finishProject = () => {
        this.finishOrUnfinishProject(true);
    }

    unfinishProject = () => {
        this.finishOrUnfinishProject(false);
    }

    finishOrUnfinishProject = (finishing) => {
        $.ajax({
            method: 'PUT',
            url: `/projects/${this.id()}/${finishing ? 'finish' : 'unfinish'}`,
            success: () => {
                alert('Successfully finished project');
                if(window.location.hostname === 'localhost') {
                    window.location.href = `//${window.location.hostname}:5000/projects/${this.id()}`;
                } else {
                    window.location.href = `//${window.location.hostname}/projects/${this.id()}`;
                }
            },
            error: (error) => {
                alert('Failed to finish project');
            }
        });
    }
}
