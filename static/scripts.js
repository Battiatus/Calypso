
document.addEventListener("DOMContentLoaded", function() {
    var dropZone = document.getElementById("drop_zone");
    var uploadForm = document.getElementById("upload_form");
    var loadingIndicator = document.getElementById("loading_indicator");

    dropZone.addEventListener("dragover", function(e) {
        e.stopPropagation();
        e.preventDefault();
        e.dataTransfer.dropEffect = "copy";
    });

    dropZone.addEventListener("drop", function(e) {
        e.stopPropagation();
        e.preventDefault();
        var files = e.dataTransfer.files;
        if (files.length) {
            document.getElementById("file").files = files;
            uploadForm.style.display = "block"; // Afficher le formulaire d'upload
        }
    });

    uploadForm.addEventListener("submit", function(e) {
        e.preventDefault();
        var formData = new FormData(uploadForm);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/");
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Conversion réussie, masquer l'indicateur de chargement
                loadingIndicator.style.display = "none";
            } else {
                // Gérer les erreurs
                alert("Une erreur s'est produite lors de la conversion.");
            }
        };
        // Afficher l'indicateur de chargement avant d'envoyer la requête
        loadingIndicator.style.display = "block";
        xhr.send(formData);
    });
});
