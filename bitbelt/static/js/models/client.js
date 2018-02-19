import ko from 'knockout';

import { formatMomentDate, capitalizeFirstLetterOfEachWordAndLowercaseAllOthers } from '../utils';

export default class Client {
    constructor(client) {
        this.dateCreated = ko.observable(formatMomentDate(client.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(client.lastModified));

        this.firstName = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.firstName));
        this.lastName = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.lastName));
        this.address = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.address));
        this.city = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.city));
        this.state = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.state));
        this.zipCode = ko.observable(client.zipCode);
        this.phone = ko.observable(client.phone);
        this.email = ko.observable(client.email);
        this.isActive = ko.observable(client.isActive);
    }
}
