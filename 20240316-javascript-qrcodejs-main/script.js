// script.js
const url =  document.getElementById("urlID");
const button = document.getElementById("buttonID");
const qr = document.getElementById("qrID");

button.onclick = function(){
    qr.textContent = '';

    new QRCode(qr, {
        text:  url.value,
        width: 128,
        height: 128,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    })
};