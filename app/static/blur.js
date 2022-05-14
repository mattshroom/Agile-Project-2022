var timer = 300000;
var toggle = false;
var solved = false;
var startTime, stopTime, timeDiff, score;

var logo = document.getElementById('logo');

// function blurOnStart(){
//     logo.classList.add('startingBlur')
// }

function unblurStart(){
    if(!toggle){
        toggle = true;
        startTime = performance.now();
        logo.classList.add('unBlur');
        logo.classList.toggle('startingBlur');
    }
    if(solved){
        stopTime = performance.now();
        timeDiff = stopTime - startTime;
        score = calculateScore(guessNum, timeDiff);

    }
}

function calculateScore(guessNum, timeDiff){
    const baseScore = 100000;
    multiplier = (timeDiff * guessNum) / 15;
    var score = baseScore - multiplier;
    return score;

}


