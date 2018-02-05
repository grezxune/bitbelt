import ko from 'knockout';

export default class Client {
    constructor(client) {
        this.firstName = ko.observable(client.firstName);
        this.lastName = ko.observable(client.lastName);
        this.address = ko.observable(client.address);
        this.city = ko.observable(client.city);
        this.state = ko.observable(client.state);
        this.zipCode = ko.observable(client.zipCode);
        this.phone = ko.observable(client.phone);
        this.email = ko.observable(client.email);
    }
}
