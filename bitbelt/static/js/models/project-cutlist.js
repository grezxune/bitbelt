import ko from 'knockout';
import _ from 'lodash';

import Project from './project';
import CutlistItem from './cutlist-item';
import { convertDecimalToFraction, combineObjectKeysAddValues } from '../utils';

export default class ProjectCutlist {
    constructor(project) {
        if (!project) {
            throw "the parameter 'project' must be provided";
        }

        this.project = ko.observable(new Project(project));
        this.cutlistItems = ko.observableArray(
            this.project()
                .cabinetOpenings()
                .map(
                    opening =>
                        new CutlistItem(opening, this.project().defaultValues)
                )
        );

        this.clientDisplay = ko.computed(() => {
            return `Client ${this.project()
                .client()
                .firstName()} ${this.project()
                .client()
                .lastName()}`;
        });

        this.projectNameDisplay = ko.computed(() => {
            return `${this.project().name()}`;
        });

        this.woodSpeciesDisplay = ko.computed(() => {
            return `Wood Species: ${this.project().woodSpecies()}`;
        });

        this.railDefaultWidthDisplay = ko.computed(() => {
            const railsWithHiddenWidths = this.cutlistItems().reduce(
                (accumulated, current) =>
                    accumulated +
                    current.rails().filter(rail => !rail.showWidth()).length,
                0
            );

            if (railsWithHiddenWidths > 0) {
                return `Default Width: ${convertDecimalToFraction(
                    this.project()
                        .defaultValues()
                        .topRailWidth()
                )}`;
            }
        });

        this.stileDefaultWidthDisplay = ko.computed(() => {
            const stilesWithHiddenWidths = this.cutlistItems().reduce(
                (accumulated, current) =>
                    accumulated +
                    current.stiles().filter(stile => !stile.showWidth()).length,
                0
            );

            if (stilesWithHiddenWidths > 0) {
                return `Default Width: ${convertDecimalToFraction(
                    this.project()
                        .defaultValues()
                        .leftStileWidth()
                )}`;
            }
        });

        this.centerRailDefaultWidthDisplay = ko.computed(() => {
            const centerRailsWithHiddenWidths = this.cutlistItems().reduce(
                (accumulated, current) =>
                    accumulated +
                    current
                        .centerRails()
                        .filter(centerRail => !centerRail.showWidth()).length,
                0
            );

            if (
                centerRailsWithHiddenWidths > 0 &&
                this.project().totalNumberOfCenterRails() > 0
            ) {
                return `Default Width: ${convertDecimalToFraction(
                    this.project()
                        .defaultValues()
                        .centerRailWidth()
                )}`;
            }
        });

        this.stileLinearFootageDisplay = ko.computed(() => {
            const stileLinearFootage = combineObjectKeysAddValues(
                this.cutlistItems().map(item => item.stileLinearFeet())
            );

            const keys = Object.keys(stileLinearFootage);

            return keys.map(key => {
                return `${convertDecimalToFraction(
                    stileLinearFootage[key] / 12
                )}' @ ${convertDecimalToFraction(key)}''`;
            });
        });

        this.railLinearFootageDisplay = ko.computed(() => {
            const railLinearFootage = combineObjectKeysAddValues(
                this.cutlistItems().map(item => item.railLinearFeet())
            );

            const keys = Object.keys(railLinearFootage);

            return keys.map(key => {
                return `${convertDecimalToFraction(
                    railLinearFootage[key] / 12
                )}' @ ${convertDecimalToFraction(key)}''`;
            });
        });

        this.centerRailLinearFootageDisplay = ko.computed(() => {
            const centerRailLinearFootage = combineObjectKeysAddValues(
                this.cutlistItems().map(item => item.centerRailLinearFeet())
            );

            const keys = Object.keys(centerRailLinearFootage);

            return keys.map(key => {
                return `${convertDecimalToFraction(
                    centerRailLinearFootage[key] / 12
                )}' @ ${convertDecimalToFraction(key)}''`;
            });
        });
    }

    printPage = () => {
        window.print();
    };
}
