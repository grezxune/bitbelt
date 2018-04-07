import ko from 'knockout';
import $ from 'jquery';

import {
    formatMomentDate,
    capitalizeFirstLetterOfEachWordAndLowercaseAllOthers
} from '../utils';

export default class Client {
    constructor(client) {
        this.dateCreated = ko.observable(formatMomentDate(client.dateCreated));
        this.lastModified = ko.observable(
            formatMomentDate(client.lastModified)
        );

        this.id = ko.observable(client.id);
        this.firstName = ko.observable(
            capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(
                client.firstName
            )
        );
        this.lastName = ko.observable(
            capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(
                client.lastName
            )
        );
        this.address = ko.observable(
            capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.address)
        );
        this.city = ko.observable(
            capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.city)
        );
        this.state = ko.observable(
            capitalizeFirstLetterOfEachWordAndLowercaseAllOthers(client.state)
        );
        this.zipCode = ko.observable(client.zipCode);
        this.phone = ko.observable(client.phone);
        this.email = ko.observable(client.email);
        this.isActive = ko.observable(client.isActive);
    }

    activateClient = () => {
        this.activateOrDeactivateClient(true);
    };

    deactivateClient = () => {
        this.activateOrDeactivateClient(false);
    };

    removeClient = () => {
        const confirmation = confirm(
            `Are you sure you want to remove ${this.firstName()} ${this.lastName()}? This is NON REVERSIBLE!`
        );

        if (confirmation) {
            const result = fetch(`/clients/${this.id()}/remove`, {
                method: 'PUT',
                credentials: 'same-origin'
            }).then(response => location.reload());
        }
    };

    activateOrDeactivateClient = activating => {
        $.ajax({
            method: 'PUT',
            url: `/clients/${this.id()}/${
                activating ? 'activate' : 'deactivate'
            }`,
            success: () => {
                location.reload();
            },
            error: error => {
                alert('Failed to activate/deactivate client');
            }
        });
    };
}
