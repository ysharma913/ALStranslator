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
    let fileName = "";
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/index.php",
        data: { 
            imgData: image
        }
    }).done(function(o) {
        console.log(o);
        fileName = o;
        console.log('saved'); 
        classifyImage(fileName);
    });
}

function classifyImage(fileName) {
    console.log(window.location.host);
    dict = JSON.stringify({'fileName': fileName});
    console.log(dict);
    $.ajax({
        type: "POST",
        url: "/classify",
        headers: "Access-Control-Allow-Origin: *",
        data: dict,
        dataType: 'json',
        contentType: "application/json",
        success: function(data){
            console.log(data);
            let box = document.getElementById('box');
            document.getElementById('classified').innerText += data;
            let but = document.createElement("button");
            but.innerHTML = "Take Another Picture";
            but.setAttribute('onclick','window.location.reload()');
            box.appendChild(but);
            
            // <button id="refresh" onclick="window.location.reload();">Take Another Picture</button>
        }
    });
}

startWebCam();