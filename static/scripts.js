document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector('form');
    var dropZone = document.getElementById("drop_zone");
    var spinner = document.getElementById("spinner"); // Assurez-vous d'avoir un élément avec l'id "spinner"

    dropZone.addEventListener("dragover", function(e) {
        e.stopPropagation();
        e.preventDefault();
        e.dataTransfer.dropEffect = "copy"; // Affiche l'icône de copie
    });

    dropZone.addEventListener("drop", function(e) {
        e.stopPropagation();
        e.preventDefault();
        var files = e.dataTransfer.files;
        if (files.length) {
            document.getElementById("file").files = files;
            spinner.style.display = "block"; // Affiche le spinner
            form.submit(); // Soumet le formulaire
        }
    });

    form.onsubmit = function() {
        spinner.style.display = "block"; // Affiche le spinner lors de la soumission du formulaire
    };
});
