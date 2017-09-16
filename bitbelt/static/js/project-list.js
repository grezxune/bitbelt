$(document).ready(function() {
    $(document).on('click', '.project', function(e) {
        window.location.href = '/project/' + e.currentTarget.id;
    });
});
