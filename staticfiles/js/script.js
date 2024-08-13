//* Delete confirmation button //
document.addEventListener('DOMContentLoaded', function() {
    var forms = document.querySelectorAll('.delete-note-form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event){
            event.preventDefault();
            
            var confirmed = confirm("Are you sure you want to delete this note?");
            if (confirmed) {
                form.submit();
            } else {
                alert("Note deletion cancelled.");
            }
        });
    });
});
