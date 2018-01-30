import ko from 'knockout';

export default class CabinetOpening {
    constructor(cabinetOpening) {
        this.id = ko.observable(cabinetOpening.id);

        this.numberOfOpenings = ko.observable(cabinetOpening.numberOfOpenings);
        this.numberOfDoors = ko.observable(cabinetOpening.numberOfDoors);
        this.openingWidth = ko.observable(cabinetOpening.openingWidth);
        this.openingHeight = ko.observable(cabinetOpening.openingHeight);
        this.middleGap = ko.observable(cabinetOpening.middleGap);

        this.leftStileWidth = ko.observable(cabinetOpening.leftStileWidth);
        this.rightStileWidth = ko.observable(cabinetOpening.rightStileWidth);
        this.topRailWidth = ko.observable(cabinetOpening.topRailWidth);
        this.bottomRailWidth =  ko.observable(cabinetOpening.bottomRailWidth);
        this.leftOverlay = ko.observable(cabinetOpening.leftOverlay);
        this.rightOverlay = ko.observable(cabinetOpening.rightOverlay);
        this.topOverlay = ko.observable(cabinetOpening.topOveraly);
        this.bottomOverlay = ko.observable(cabinetOpening.bottomOverlay);
        this.panelGap = ko.observable(cabinetOpening.panelGap);
        this.tennonLength = ko.observable(cabinetOpening.tennonLength);

        this.calculateDoorWidth = ko.computed(() => {
            let width = this.openingWidth() + this.leftOverlay() + this.rightOverlay();
            // let width = opening.leftStileWidth() + opening.rightStileWidth();
            // width += opening.tennonLength() + opening.tennonLength();
            // width +=

            return width;
        });
    }
}