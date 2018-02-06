import ko from 'knockout';

import { formatMomentDate } from '../utils';

export default class DefaultValues {
    constructor(defaultValues) {
        this.dateCreated = ko.observable(formatMomentDate(defaultValues.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(defaultValues.lastModified));

        this.leftStileWidth = ko.observable(defaultValues.leftStileWidth);
        this.rightStileWidth = ko.observable(defaultValues.rightStileWidth);
        this.topRailWidth = ko.observable(defaultValues.topRailWidth);
        this.bottomRailWidth =  ko.observable(defaultValues.bottomRailWidth);
        this.leftOverlay = ko.observable(defaultValues.leftOverlay);
        this.rightOverlay = ko.observable(defaultValues.rightOverlay);
        this.topOverlay = ko.observable(defaultValues.topOveraly);
        this.bottomOverlay = ko.observable(defaultValues.bottomOverlay);
        this.panelGap = ko.observable(defaultValues.panelGap);
        this.middleGap = ko.observable(defaultValues.middleGap);
        this.tennonLength = ko.observable(defaultValues.tennonLength);
        this.centerRailWidth = ko.observable(defaultValues.centerRailWidth);
    }
}