import ko from 'knockout';

import { formatMomentDate } from '../utils';

export default class UserSettings {
    constructor(settings) {
        this.dateCreated = ko.observable(formatMomentDate(settings.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(settings.lastModified));

        this.roughSawnOverestimate = ko.observable(settings.roughSawnOverestimate);
    }
}