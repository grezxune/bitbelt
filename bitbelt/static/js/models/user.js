import ko from 'knockout';

import UserSettings from './user-settings';
import Project from './project';
import Client from './client';

import { formatMomentDate, capitalizeFirstLetterOfEachWordAndLowercaseAllOthers } from '../utils';

export default class User {
    constructor(user) {
        this.dateCreated = ko.observable(formatMomentDate(user.dateCreated));
        this.lastModified = ko.observable(formatMomentDate(user.lastModified));

        this.userId = ko.observable(user.id);
        this.firstName = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(user.firstName));
        this.lastName = ko.observable(capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(user.lastName));
        this.email = ko.observable(user.email);
        this.settings = ko.observable(new UserSettings(user.settings));
        this.projects = ko.observableArray(user.projects.map(proj => new Project(proj)));
        this.clients = ko.observableArray(user.clients.map(client => new Client(client)));
    }
}