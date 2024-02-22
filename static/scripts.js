document.getElementById('drop_zone').addEventListener('dragover', function(event) {
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
});

document.getElementById('drop_zone').addEventListener('drop', function(event) {
    event.stopPropagation();
    event.preventDefault();
    const files = event.dataTransfer.files;
    const formData = new FormData();
    formData.append('file', files[0]);  // Exemple avec un seul fichier
    formData.append('format', 'json');  // Exemple : spécifiez le format souhaité ici

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = files[0].name + '.json';  // Assurez-vous que cela correspond au format de fichier retourné
        document.body.appendChild(a); // Nécessaire pour Firefox
        a.click();
        a.remove();
    })
    .catch(error => console.error('Error:', error));
});
