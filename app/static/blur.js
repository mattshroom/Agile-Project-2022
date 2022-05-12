var timer = 3000;
var blurAmount = 100
var toggle = false;
var solved = false;

var logo = document.getElementById('logo');

function blurOnStart(){
    logo.classList.add('startingBlur')
    // alert("Time's Up!");
}

function unblurStart(){
    logo.classList.add('unBlur');
    logo.classList.toggle('startingBlur')
}
