$(document).ready(function() {
    $(document).on('click', '.project', function(e) {
        window.location.href = '/projects/' + e.currentTarget.id;
    });
});
