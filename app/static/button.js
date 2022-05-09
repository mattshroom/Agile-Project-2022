var toggle = false;
function toggleText() {
    toggle = !toggle;
    let text;
    if (toggle) {
        text = "You pressed the button!";
    }
    else {
        text = "";
    }
    document.getElementById("textBox").innerHTML = text;
}

function blurImage(){
    toggle = !toggle;
    if(toggle){
        document.getElementById("image").style.filter = "blur(25px)";
    }
    else{
        document.getElementById("image").style.filter = "blur(0px)";
    }
}

document.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("myButton").click();
    }
});