import ko from 'knockout';

export default class CabinetDoor {
    constructor(cabinetOpening) {
        this.cabinetOpening = ko.observable(cabinetOpening);

        this.getWidth = ko.computed(() => {
            const opening = this.cabinetOpening();

            let width = opening.openingWidth() + opening.leftOverlay() + opening.rightOverlay();
            // let width = opening.leftStileWidth() + opening.rightStileWidth();
            // width += opening.tennonLength() + opening.tennonLength();
            // width +=

            return width;
        });
    }
}
