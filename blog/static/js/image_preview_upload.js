// image_upload_preview.js

document.getElementById("imageUpload").addEventListener("change", function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
        var previewImage = document.getElementById("previewImage");
        previewImage.src = event.target.result;
        previewImage.style.display = "block";
    };

    reader.readAsDataURL(file);
});
