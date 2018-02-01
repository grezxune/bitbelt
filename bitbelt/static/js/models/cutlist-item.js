import ko from 'knockout';

import Rail from './rail';
import Stile from './Stile';

export default class CutlistItem {
    constructor(cabinetOpening, defaultValues) {
        this.cabinetOpening = ko.observable(cabinetOpening);
        this.defaultValues = defaultValues;

        this.doorWidth = this.cabinetOpening().calculateDoorWidth;
        this.doorHeight = this.cabinetOpening().calculateDoorHeight;
        this.doorQuantity = this.cabinetOpening().totalNumberOfDoors;

        this.doorDisplay = ko.computed(() => {
            return `${this.doorWidth()} x ${this.doorHeight()} (${this.doorQuantity()})`;
        });

        this.panelWidth = this.cabinetOpening().calculatePanelWidth;
        this.panelHeight = this.cabinetOpening().calculatePanelHeight;
        this.panelQuantity = this.cabinetOpening().totalNumberOfPanels;

        this.panelDisplay = ko.computed(() => {
            return `${this.panelWidth()} x ${this.panelHeight()} (${this.panelQuantity()})`;
        });

        this.rails = ko.computed(() => {
            let rails = [];
            const railWidthDefaultsVary = this.defaultValues().topRailWidth() != this.defaultValues().bottomRailWidth();
            const topRailWidthIsDefault = this.cabinetOpening().topRailWidth() == this.defaultValues().topRailWidth();
            const bottomRailWidthIsDefault = this.cabinetOpening().bottomRailWidth() == this.defaultValues().bottomRailWidth();

            const topRail = new Rail(this.cabinetOpening().topRailWidth(),
                                        this.cabinetOpening().calculateRailLength(),
                                        !topRailWidthIsDefault || railWidthDefaultsVary,
                                        this.cabinetOpening().totalNumberOfTopRails());

            const bottomRail = new Rail(this.cabinetOpening().bottomRailWidth(),
                                        this.cabinetOpening().calculateRailLength(),
                                        !bottomRailWidthIsDefault || railWidthDefaultsVary,
                                        this.cabinetOpening().totalNumberOfBottomRails());

            if(topRail.equals(bottomRail)) {
                rails.push(topRail.merge(bottomRail));
            } else {
                rails.push(topRail);
                rails.push(bottomRail);
            }

            return rails;
        });

        this.railDisplays = ko.computed(() => {
            const displays = this.rails().map(rail => `${rail.showWidth() ? `${rail.width()} x ` : ''}${rail.length()} (${rail.quantity()})`);
            return displays;
        });

        this.stiles = ko.computed(() => {
            let stiles = [];
            const stileWidthDefaultsVary = this.defaultValues().leftStileWidth() != this.defaultValues().rightStileWidth();
            const leftStileWidthIsDefault = this.cabinetOpening().leftStileWidth() == this.defaultValues().leftStileWidth();
            const rightStileWidthIsDefault = this.cabinetOpening().rightStileWidth() == this.defaultValues().rightStileWidth();

            const leftStile = new Stile(this.cabinetOpening().leftStileWidth(),
                                        this.cabinetOpening().calculateStileLength(),
                                        !leftStileWidthIsDefault || stileWidthDefaultsVary,
                                        this.cabinetOpening().totalNumberOfLeftStiles());

            const rightStile = new Stile(this.cabinetOpening().rightStileWidth(),
                                            this.cabinetOpening().calculateStileLength(),
                                            !rightStileWidthIsDefault || stileWidthDefaultsVary,
                                            this.cabinetOpening().totalNumberOfRightStiles());

            if(leftStile.equals(rightStile)) {
                stiles.push(leftStile.merge(rightStile));
            } else {
                stiles.push(leftStile);
                stiles.push(rightStile);
            }

            return stiles;
        });

        this.stileDisplays = ko.computed(() => {
            const displays = this.stiles().map(stile => `${stile.showWidth() ? `${stile.width()} x ` : ''}${stile.length()} (${stile.quantity()})`);
            return displays;
        });

        this.centerRails = ko.computed(() => {
            let centerRails = [];
            const centerRailWidthIsDefault = this.cabinetOpening().centerRailWidth() == this.defaultValues().centerRailWidth();

            const centerRail = new Rail(this.cabinetOpening().centerRailWidth(),
                                        this.cabinetOpening().calculateCenterRailLength(),
                                        !centerRailWidthIsDefault,
                                        this.cabinetOpening().totalNumberOfCenterRails());
            
            centerRails.push(centerRail);

            return centerRails;
        });

        this.centerRailDisplays = ko.computed(() => {
            const displays = this.centerRails().map(centerRail =>
                `${this.cabinetOpening().totalNumberOfCenterRails() > 0 ?
                    `${centerRail.showWidth() ?
                        `${centerRail.width()} x ` : ''}${centerRail.length()} (${centerRail.quantity()})` : 'N/A'}`);
            return displays;
        });
    }
}