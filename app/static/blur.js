var timer = 300000;
var toggle = false;
var solved = false;
var startTime, stopTime, timeDiff, guessNum, score;
let id = Math.floor((Math.random() * 19) + 1);

// function blurOnStart(){
//     logo.classList.add('startingBlur')
// }

function unblurStart(){

    var logo1 = document.querySelector("#imgID");
    if(!toggle){
        toggle = true;
        startTime = performance.now();
        console.log(startTime)
        console.log("Starting to unblur!")
        logo1.classList.add('unBlur');
        logo1.classList.toggle('startingBlur');
        
    }

    console.log("Waiting...")

    if(performance.now() - startTime != 20000){ // in ms
        guessNum = 2;
        console.log("Time's Up!")
        stopTime = performance.now();
        timeDiff = stopTime - startTime;
        score = setInterval(calculateScore,1000,guessNum, timeDiff);
        console.log("Score is: ", score)
        solved = true;
    }
}

function calculateScore(guessNum, timeDiff){
    const baseScore = 100000;
    multiplier = (timeDiff * guessNum) / 15;
    var score = baseScore - multiplier;
    return score;
}

function jsonImage() {
   fetch('../static/logo_json.json')
      .then(response => response.json())
      .then(data => {
         //document.querySelector("#debug").innerText = data.logos[0].logo_link
         var image = data.logos[id].logo_link;
         document.getElementById("imgID").src= image;
      })
}

window.onload = function() {
    jsonImage()
}