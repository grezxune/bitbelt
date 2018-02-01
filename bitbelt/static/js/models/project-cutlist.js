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

        this.clientDisplay = ko.computed(() => {
            return `Cutlist for ${this.project().client().firstName()} ${this.project().client().lastName()}`;
        });

        this.projectNameDisplay = ko.computed(() => {
            return `Project "${this.project().name()}"`;
        });

        this.railDefaultWidthDisplay = ko.computed(() => {
            const railsWithHiddenWidths = this.cutlistItems().reduce((accumulated, current) => accumulated + current.rails().filter(rail => !rail.showWidth()).length, 0);

            if (railsWithHiddenWidths > 0) {
                return `Default Width: ${this.project().defaultValues().topRailWidth()}`;
            }
        });

        this.stileDefaultWidthDisplay = ko.computed(() => {
            const stilesWithHiddenWidths = this.cutlistItems().reduce((accumulated, current) => accumulated + current.stiles().filter(stile => !stile.showWidth()).length, 0);

            if (stilesWithHiddenWidths > 0) {
                return `Default Width: ${this.project().defaultValues().leftStileWidth()}`;
            }
        });

        this.centerRailDefaultWidthDisplay = ko.computed(() => {
            const centerRailsWithHiddenWidths = this.cutlistItems().reduce((accumulated, current) => accumulated + current.centerRails().filter(centerRail => !centerRail.showWidth()).length, 0);

            if (centerRailsWithHiddenWidths > 0 && this.project().totalNumberOfCenterRails() > 0) {
                return `Default Width: ${this.project().defaultValues().centerRailWidth()}`;
            }
        });
    }

    printPage = () => {
        window.print();
    }
}
