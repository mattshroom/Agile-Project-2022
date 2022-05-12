var timer = 3000;
var blurAmount = 100
var toggle = false;
var solved = false;

var logo = document.getElementById('logo');
// img.addEventListener('onload',blurTime);

function blurOnStart(){
    logo.classList.add('startingBlur')
    // alert("Time's Up!");
}

function unblurStart(){
    // document.getElementById("image").style= "blur(12px)";
    logo.classList.add('unBlur');
    logo.classList.toggle('startingBlur')
}

function blurImageClick(){
    toggle = !toggle;
    
    // if(toggle){
    //     document.getElementById("image").style.filter = "blur(25px)";
    // }
    // else{
    //     document.getElementById("image").style.filter = "blur(0px)";
    // }
    



}
