const baseScore = 100000;
var toggle = false;
var solved = false;
var startTime, stopTime, timeDiff, guessNum, score;
let seed;
let guessCount = 0;

let numLogos = 19;

const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 10;
const ALERT_THRESHOLD = 5;

const COLOR_CODES = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold: WARNING_THRESHOLD
  },
  alert: {
    color: "red",
    threshold: ALERT_THRESHOLD
  }
};


function seedImage() {
  today = new Date();
  epoch = new Date(0);
  seed = today - epoch;
  var fullDaysSinceEpoch = Math.floor(seed/8.64e7);
  console.log(fullDaysSinceEpoch);

  return fullDaysSinceEpoch;
}

// JS Math.random function can't be seeded, so using xorShift PRNG
// fdse stands for fullDaysSinceEpoch (seeded based on the day)
function xorShift(fdse) {
    fdse ^= fdse << 13; fdse ^= fdse >> 17; fdse ^= fdse << 5;
    return fdse;
}

let imageSeed = seedImage();
let id = xorShift(imageSeed);
// the modulus number MUST = number of objects in logo_json.json
id = (id%numLogos)+1


const TIME_LIMIT = 120;
let timePassed = 0;
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;

document.getElementById("app").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label" class="base-timer__label">${formatTime(
    timeLeft
  )}</span>
</div>
`;

//startTimer();


function onTimesUp() {
  clearInterval(timerInterval);
  removeBlur();
  document.getElementById("submitButton").disabled = true;
  document.getElementById("submit").disabled = true;
  document.getElementById("userGuess").disabled = true;
}

function calculateScore(guessNum, timeTaken) {
  if(!solved){
      var score = 0
  }
  else if(solved){
      var score = baseScore - (5/12)*timeTaken - (50000-(5/guessNum)*10000);
  }
  return Math.round(score);
}

function startTimer() {
  timerInterval = setInterval(() => {
    timePassed = timePassed += 1;
    timeLeft = TIME_LIMIT - timePassed;
    document.getElementById("base-timer-label").innerHTML = formatTime(timeLeft);
    setCircleDasharray();
    setRemainingPathColor(timeLeft);

    // Solved before times up
    if (solved){
      onTimesUp();
      score = calculateScore(guessCount, timePassed*1000);
      console.log(score);
      temp = 'You guessed it right!';
      document.getElementById('exampleModalLabel').innerHTML = temp;
      $('#exampleModal').modal('show'); 
      
    }

    // Times up
    else if (timeLeft === 0) {
      onTimesUp();
      score = calculateScore(guessCount,timePassed*1000);
      console.log(score)
      temp = "Time's up!";
      document.getElementById('exampleModalLabel').innerHTML = temp;
      $('#exampleModal').modal('show');
    }

    else if (!solved && guessCount >= 5){
      
    }
  }, 1000);
}

function formatTime(time) {
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  return `${minutes}:${seconds}`;
}

function setRemainingPathColor(timeLeft) {
  const { alert, warning, info } = COLOR_CODES;
  if (timeLeft <= alert.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(warning.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(alert.color);
  } else if (timeLeft <= warning.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(info.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(warning.color);
  }
}

function calculateTimeFraction() {
  const rawTimeFraction = timeLeft / TIME_LIMIT;
  return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
}

function setCircleDasharray() {
  const circleDasharray = `${(
    calculateTimeFraction() * FULL_DASH_ARRAY
  ).toFixed(0)} 283`;
  document
    .getElementById("base-timer-path-remaining")
    .setAttribute("stroke-dasharray", circleDasharray);
}

function unblurStart() {
    
    var logo1 = document.querySelector("#imgID");
    if (!toggle) {
        startTimer();
        toggle = true;
        console.log("Starting to unblur!")
        logo1.classList.add('unBlur');
        logo1.classList.toggle('startingBlur');
    }
    console.log("Waiting...")
}

function removeBlur(){
    var logo1 = document.querySelector("#imgID");
    logo1.classList.toggle('unBlur');
    logo1.classList.toggle('unBlurQuick')
    // logo1.classList.toggle('')
}


function jsonImage() {
    // let id = Math.floor((Math.random() * 19) + 1);
    fetch('../static/logo_json.json')
        .then(response => response.json())
        .then(data => {
            //document.querySelector("#debug").innerText = data.logos[0].logo_link
            var image = data.logos[id].logo_link;
            document.getElementById("imgID").src = image;
        })
}


function guessCompare() {
    
    if(solved){
        console.log("You've already won!")
        
    }

    else if(document.getElementById('userGuess').value === ''){
      alert("Empty Input");
      
    }

    else if(!solved && guessCount < 6){
      let guess = document.getElementById("userGuess").value;
      fetch('../static/logo_json.json') //get logoname from json file
          .then(response => response.json())
          .then(data => {
              //document.querySelector("#debug").innerText = data.logos[0].logo_link
              var name = data.logos[id].name;
              let result = name.localeCompare(guess); //compare function
              guessCount += 1
              if (guessCount <= 5 && result == 0) { //0 mean guess was right and anything else is wrong
                  //alert("correct");
                  const y = document.createElement('div');
                  y.innerHTML = guess;
                  y.classList.add("correct");
                  document.getElementById("superdiv").appendChild(y);
                  const correctImg = document.createElement("img");
                  correctImg.src = "../static/logos/Correct.png";
                  correctImg.setAttribute("height", "40");
                  correctImg.setAttribute("width", "40");
                  document.getElementsByClassName("correct")[0].appendChild(correctImg);
                  solved = true;
                  console.log("Winner in ", guessCount)
                  document.getElementById("submitButton").disabled = true;
                  document.getElementById("submit").disabled = true;
                  document.getElementById("userGuess").disabled = true;
                  
              }

              else if(guessCount < 5){
                  const n = document.createElement('div');
                  n.innerHTML = guess;
                  n.classList.add("incorrect");
                  document.getElementById("superdiv").appendChild(n);
                  const wrongImg = document.createElement("img");
                  wrongImg.src = "../static/logos/Incorrect.png";

                  wrongImg.setAttribute("height", "40");
                  wrongImg.setAttribute("width", "40");

                  document.getElementsByClassName("incorrect")[guessCount-1].appendChild(wrongImg);
                  console.log(guessCount);
              }
              else if(guessCount === 5 && !solved){
                  const n = document.createElement('div');
                  n.innerHTML = guess;
                  n.classList.add("incorrect");
                  document.getElementById("superdiv").appendChild(n);
                  const wrongImg = document.createElement("img");
                  wrongImg.src = "../static/logos/Incorrect.png";

                  wrongImg.setAttribute("height", "40");
                  wrongImg.setAttribute("width", "40");

                  document.getElementsByClassName("incorrect")[guessCount-1].appendChild(wrongImg);
                  console.log(guessCount);
                  onTimesUp();
                  score = calculateScore(guessCount, timePassed*1000);
                  console.log("Score:", score)
                  console.log("Game Over Man, Game Over");
              }
              else if(guessCount >= 6){
                  // Hit Max guesses and still not solved
                  // onTimesUp();
                  // score = calculateScore(guessCount, timePassed*1000);
                  // console.log("Score:",score);
                  console.log("Too many guesses, try again tomorrow!");
              }

              if (solved) {
                temp = 'You guessed it right!';
                document.getElementById('exampleModalLabel').innerHTML = temp;
                $('#exampleModal').modal('show'); 
              }
              else if (!solved && guessCount >= 5){
                temp = 'Wrong, It was ' + name;
                document.getElementById('exampleModalLabel').innerHTML = temp;
                $('#exampleModal').modal('show'); 
              }
          })
        }
        document.getElementById('userGuess').value = '';

}

var input = document.getElementById("userGuess");
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("submit").click();
  }
});

// Start the ReadyModal on load
$(document).ready(function(){
  $("#readyModal").modal('show');
});

