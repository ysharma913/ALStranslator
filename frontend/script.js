const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const snapSoundElement = document.getElementById('snapSound');
const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);

function startWebCam() {
    webcam.start()
    .then(result =>{
        console.log("webcam started");
    })
    .catch(err => {
        console.log(err);
    });
}

function snapPicture() {
    let picture = webcam.snap();
    webcam.stop();
    document.getElementById('pictureButton').remove();
    webcamElement.remove();
    console.log(picture);
    canvasElement.src = picture;
    downloadImage(picture);
}

function downloadImage(image) {
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/index.php",
        data: { 
            imgData: image
        }
    }).done(function(o) {
        console.log('saved'); 
    });
}

startWebCam();