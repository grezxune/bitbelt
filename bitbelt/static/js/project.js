$(document).ready(function() {
    $(document).on('click', '.btn-add-door', function(e) {
        window.location.href = '/projects/' + e.currentTarget.id + '/cabinet-opening/create';
    });
});
