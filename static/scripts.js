document.getElementById('drop_zone').addEventListener('click', function() {
    document.getElementById('file_input').click();
});

document.getElementById('drop_zone').addEventListener('dragover', function(event) {
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
});

document.getElementById('drop_zone').addEventListener('drop', function(event) {
    event.stopPropagation();
    event.preventDefault();
    const files = event.dataTransfer.files;
    console.log(files);
    // Ici, ajoutez la logique pour envoyer les fichiers au serveur
});

document.getElementById('upload_btn').addEventListener('click', function() {
    // Logique pour télécharger le résultat de la conversion
});
