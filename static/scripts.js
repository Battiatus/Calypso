// static/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    var dropZone = document.getElementById("drop_zone");
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
            document.getElementById("submit").click();
        }
    });
});
