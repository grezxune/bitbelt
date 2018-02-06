import ko from 'knockout';
import $ from 'jquery';

import { formatMomentDate } from '../utils';

export default class CabinetOpening {
    constructor(cabinetOpening, projectId) {
        this.dateCreated = ko.observable(formatMomentDate(cabinetOpening.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(cabinetOpening.lastModified));

        this.projectId = ko.observable(projectId);
        this.id = ko.observable(cabinetOpening.id);

        this.numberOfOpenings = ko.observable(cabinetOpening.numberOfOpenings);
        this.numberOfDoors = ko.observable(cabinetOpening.numberOfDoors);
        this.numberOfPanelsPerDoor = ko.observable(cabinetOpening.numberOfPanelsPerDoor);
        this.openingWidth = ko.observable(cabinetOpening.openingWidth);
        this.openingHeight = ko.observable(cabinetOpening.openingHeight);

        this.leftStileWidth = ko.observable(cabinetOpening.leftStileWidth);
        this.rightStileWidth = ko.observable(cabinetOpening.rightStileWidth);
        this.topRailWidth = ko.observable(cabinetOpening.topRailWidth);
        this.bottomRailWidth =  ko.observable(cabinetOpening.bottomRailWidth);
        this.leftOverlay = ko.observable(cabinetOpening.leftOverlay);
        this.rightOverlay = ko.observable(cabinetOpening.rightOverlay);
        this.topOverlay = ko.observable(cabinetOpening.topOverlay);
        this.bottomOverlay = ko.observable(cabinetOpening.bottomOverlay);
        this.panelGap = ko.observable(cabinetOpening.panelGap);
        this.middleGap = ko.observable(cabinetOpening.middleGap);
        this.tennonLength = ko.observable(cabinetOpening.tennonLength);
        this.centerRailWidth = ko.observable(cabinetOpening.centerRailWidth);
        this.centerRailHorizontal = ko.observable(cabinetOpening.centerRailHorizontal);
        this.roughSawnOverestimate = ko.observable(cabinetOpening.roughSawnOverestimate);

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
            let centerRailLength;

            if(this.centerRailHorizontal()) {
                // Horizontal Center Rail
                centerRailLength = this.calculateDoorWidth();
                centerRailLength -= this.leftStileWidth();
                centerRailLength -= this.rightStileWidth();
                centerRailLength += this.tennonLength() * 2;
            } else {
                // Vertical Center Rail
                centerRailLength = this.calculateDoorHeight();
                centerRailLength -= this.topRailWidth();
                centerRailLength -= this.bottomRailWidth();
                centerRailLength += this.tennonLength() * 2;
            }

            return centerRailLength;
        });

        this.totalNumberOfCenterRails = ko.computed(() => {
            return this.totalNumberOfDoors() * (this.numberOfPanelsPerDoor() - 1);
        });

        /********************************/
        /*** PANEL COMPUTED FUNCTIONS ***/
        /********************************/

        this.calculatePanelWidth = ko.computed(() => {
            let panelWidth;

            if(this.centerRailHorizontal()) {
                // Horizontal Center Rail
                panelWidth = this.calculateInnerDoorWidth();
                panelWidth += this.tennonLength() * 2;
                panelWidth -= this.panelGap() * 2;
            } else {
                // Vertical Center Rail
                panelWidth = this.calculateInnerDoorWidth() / this.numberOfPanelsPerDoor();
                panelWidth -= this.totalNumberOfCenterRails() > 0 ? this.centerRailWidth() / 2 : 0;
                panelWidth += this.tennonLength() * 2;
                panelWidth -= this.panelGap() * 2;
            }

            return panelWidth;
        });

        this.calculatePanelHeight = ko.computed(() => {
            let panelHeight;

            if(this.centerRailHorizontal()) {
                // Horizontal Center Rail
                panelHeight = this.calculateInnerDoorHeight() / this.numberOfPanelsPerDoor();
                panelHeight -= this.totalNumberOfCenterRails() > 0 ? this.centerRailWidth() / 2 : 0;
                panelHeight += this.tennonLength() * 2;
                panelHeight -= this.panelGap() * 2;
            } else {
                // Vertical Center Rail
                panelHeight = this.calculateDoorHeight();
                panelHeight -= this.topRailWidth();
                panelHeight -= this.bottomRailWidth();
                panelHeight += this.tennonLength() * 2;
                panelHeight -= this.panelGap() * 2;
            }
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
            stileLength += this.roughSawnOverestimate();
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
            $.ajax({
                method: 'DELETE',
                url: `/projects/${this.projectId()}/cabinet-openings/${this.id()}`,
                success: () => {
                    alert('Successfully removed cabinet opening');
                    if(window.location.hostname === 'localhost') {
                        window.location.href = `//${window.location.hostname}:5000/projects/${this.projectId()}`;
                    } else {
                        window.location.href = `//${window.location.hostname}/projects/${this.projectId()}`;
                    }
                },
                error: (error) => {
                    alert('Failed to remove cabinet opening');
                }
            });
        }
    }
}