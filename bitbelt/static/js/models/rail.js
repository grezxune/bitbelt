import ko from 'knockout';

export default class Rail {
    constructor(width, length, showWidth, quantity) {
        this.width = ko.observable(width);
        this.length = ko.observable(length);
        this.showWidth = ko.observable(showWidth);
        this.quantity = ko.observable(quantity);
    }

    equals = (railToCompare) => {
        return this.width() == railToCompare.width() &&
                this.length() == railToCompare.length() &&
                this.showWidth() == railToCompare.showWidth();
    }

    merge = (railToMerge) => {
        return new Rail(this.width(), this.length(), this.showWidth(), this.quantity() + railToMerge.quantity());
    }
}
