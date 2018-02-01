import ko from 'knockout';

export default class UserSettings {
    constructor(settings) {
        this.roughSawnOverestimate = ko.observable(settings.roughSawnOverestimate);
    }
}