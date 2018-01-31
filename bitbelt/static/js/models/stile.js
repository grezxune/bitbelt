import ko from 'knockout';

export default class Stile {
    constructor(width, length, showWidth, quantity) {
        this.width = ko.observable(width);
        this.length = ko.observable(length);
        this.showWidth = ko.observable(showWidth);
        this.quantity = ko.observable(quantity);
    }

    equals = (stileToCompare) => {
        return this.width() == stileToCompare.width() &&
                this.length() == stileToCompare.length() &&
                this.showWidth() == stileToCompare.showWidth();
    }

    merge = (stileToMerge) => {
        return new Stile(this.width(), this.length(), this.showWidth(), this.quantity() + stileToMerge.quantity());
    }
}
