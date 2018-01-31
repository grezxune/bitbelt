import ko from 'knockout';

export default class CabinetOpening {
    constructor(cabinetOpening) {
        this.id = ko.observable(cabinetOpening.id);

        this.numberOfOpenings = ko.observable(cabinetOpening.numberOfOpenings);
        this.numberOfDoors = ko.observable(cabinetOpening.numberOfDoors);
        this.numberOfPanelsPerDoor = ko.observable(cabinetOpening.numberOfPanelsPerDoor);
        this.openingWidth = ko.observable(cabinetOpening.openingWidth);
        this.openingHeight = ko.observable(cabinetOpening.openingHeight);
        this.middleGap = ko.observable(cabinetOpening.middleGap);

        this.leftStileWidth = ko.observable(cabinetOpening.leftStileWidth);
        this.rightStileWidth = ko.observable(cabinetOpening.rightStileWidth);
        this.topRailWidth = ko.observable(cabinetOpening.topRailWidth);
        this.bottomRailWidth =  ko.observable(cabinetOpening.bottomRailWidth);
        this.leftOverlay = ko.observable(cabinetOpening.leftOverlay);
        this.rightOverlay = ko.observable(cabinetOpening.rightOverlay);
        this.topOverlay = ko.observable(cabinetOpening.topOverlay);
        this.bottomOverlay = ko.observable(cabinetOpening.bottomOverlay);
        this.panelGap = ko.observable(cabinetOpening.panelGap);
        this.tennonLength = ko.observable(cabinetOpening.tennonLength);
        this.centerRailWidth = ko.observable(cabinetOpening.centerRailWidth);

        this.numberOfDoors.subscribe(() => {
            console.log('Updating numberOfDoors...');
        });

        /*******************************/
        /*** DOOR COMPUTED FUNCTIONS ***/
        /*******************************/

        this.calculateDoorWidth = ko.computed(() => {
            let width = this.openingWidth() + this.leftOverlay() + this.rightOverlay();
            width -= this.middleGap() * (this.numberOfDoors() - 1);
            width = width / this.numberOfDoors();
            return width;
        });

        this.calculateDoorHeight = ko.computed(() => {
            return this.openingHeight() + this.topOverlay() + this.bottomOverlay();
        });

        this.calculateInnerDoorWidth = ko.computed(() => {
            return this.calculateDoorWidth() - this.leftStileWidth() - this.rightStileWidth();
        });

        this.calculateInnerDoorHeight = ko.computed(() => {
            return this.calculateDoorHeight() - this.topRailWidth() - this.bottomRailWidth();
        });

        this.totalNumberOfDoors = ko.computed(() => {
            return this.numberOfOpenings() * this.numberOfDoors();
        });

        /**************************************/
        /*** CENTER RAIL COMPUTED FUNCTIONS ***/
        /**************************************/

        this.calculateCenterRailLength = ko.computed(() => {
            let centerRailLength = this.calculateDoorHeight();
            centerRailLength -= this.topRailWidth();
            centerRailLength -= this.bottomRailWidth();
            centerRailLength += this.tennonLength() * 2;
            centerRailLength -= this.panelGap() * 2;

            return centerRailLength;
        });

        this.totalNumberOfCenterRails = ko.computed(() => {
            return this.totalNumberOfDoors() * (this.numberOfPanelsPerDoor() - 1);
        });

        /********************************/
        /*** PANEL COMPUTED FUNCTIONS ***/
        /********************************/

        this.calculatePanelWidth = ko.computed(() => {
            let panelWidth = this.calculateInnerDoorWidth() / this.numberOfPanelsPerDoor();
            panelWidth -= this.totalNumberOfCenterRails() > 0 ? this.centerRailWidth() / 2 : 0;
            panelWidth += this.tennonLength() * 2;
            panelWidth -= this.panelGap() * 2;
            return panelWidth;
        });

        this.calculatePanelHeight = ko.computed(() => {
            let panelHeight = this.calculateDoorHeight();
            panelHeight -= this.topRailWidth();
            panelHeight -= this.bottomRailWidth();
            panelHeight += this.tennonLength() * 2;
            panelHeight -= this.panelGap() * 2;
            return panelHeight;
        });

        this.totalNumberOfPanels = ko.computed(() => {
            return this.numberOfOpenings() * this.numberOfDoors() * this.numberOfPanelsPerDoor();
        });

        /*******************************/
        /*** RAIL COMPUTED FUNCTIONS ***/
        /*******************************/

        this.calculateRailLength = ko.computed(() => {
            let railLength = this.calculateDoorWidth();
            railLength -= this.leftStileWidth();
            railLength -= this.rightStileWidth();
            railLength += this.tennonLength() * 2;
            return railLength;
        });

        this.totalNumberOfTopRails = ko.computed(() => {
            return this.totalNumberOfDoors();
        });

        this.totalNumberOfBottomRails = ko.computed(() => {
            return this.totalNumberOfDoors();
        });

        /********************************/
        /*** STILE COMPUTED FUNCTIONS ***/
        /********************************/

        this.calculateStileLength = ko.computed(() => {
            let stileLength = this.calculateDoorHeight();
            // UNCOMMENT ONCE READY
            // stileLength += this.roughSawnOverestimate();
            return stileLength;
        });

        this.totalNumberOfLeftStiles = ko.computed(() => {
            return this.totalNumberOfDoors();
        });

        this.totalNumberOfRightStiles = ko.computed(() => {
            return this.totalNumberOfDoors();
        });

        /************************/
        /*** BUTTON LISTENERS ***/
        /************************/
        this.deleteCabinetOpening = (opening) => {
            console.log('Need to delete this guy! He has an id of: ' + opening.id());
        }
    }
}