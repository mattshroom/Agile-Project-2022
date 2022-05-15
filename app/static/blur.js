var timer = 300000;
var toggle = false;
var solved = false;
var startTime, stopTime, timeDiff, guessNum, score;

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

// var countDownDate = new Date("May 15, 2022 18:14:00").getTime();

// // Update the count down every 1 second
// var x = setInterval(function() {

//   // Get today's date and time
//   var now = new Date().getTime();

//   // Find the distance between now and the count down date
//   var distance = countDownDate - now;

//   // Time calculations for days, hours, minutes and seconds
//   var days = Math.floor(distance / (1000 * 60 * 60 * 24));
//   var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);

//   // Display the result in the element with id="demo"
//   document.getElementById("demo").innerHTML = days + "d " + hours + "h "
//   + minutes + "m " + seconds + "s ";

//   // If the count down is finished, write some text
//   if (distance < 0) {
//     clearInterval(x);
//     document.getElementById("demo").innerHTML = "EXPIRED";
//   }
// }, 1000);

