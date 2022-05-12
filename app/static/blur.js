var timer = 3000;
var blurAmount = 100
var toggle = false;
var solved = false;

var logo = document.getElementById('logo');

// function blurOnStart(){
//     logo.classList.add('startingBlur')
// }

function unblurStart(){
    if(!toggle){
        toggle = true;
        logo.classList.add('unBlur');
        logo.classList.toggle('startingBlur')
    }
}
