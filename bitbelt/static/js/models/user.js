import ko from 'knockout';

export default class User {
    constructor(user) {
        this.user_id = ko.observable(user.id);
        this.first_name = ko.observable(user.firstName);
        this.last_name = ko.observable(user.lastName);
        this.email = ko.observable(user.email);
    }
}