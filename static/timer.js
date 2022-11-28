/*const timer = document.getElementById("timer");
const modeButtons = document.querySelector("[class=modeSelector]");
const pomodoroButton = document.getElementById("pomodoroButton");
const shortButton = document.getElementById("shortButton");
const longButton = document.getElementById("longButton");
const mainButton = document.getElementById("toggle");
let seconds = 0;

const TIMER = {
  POMODORO: 25,
  SHORTBREAK: 5,
  LONGBREAK: 15,
};

function changeMode(e) {
  mainButton.classList.replace("fa-stop", "fa-play");
  mainButton.dataset.paused = "true";

  for (let i = 0; i < 3; i++) {
    e.path[1].children[i].classList.remove("active");
  }
  e.target.classList.add("active");

  let mode = e.target.dataset.mode;
  timer.dataset.mode = mode;

  if (timer.dataset.mode === "pomodoro") {
    timer.innerHTML = `${TIMER.POMODORO}:00`;
  } else if (timer.dataset.mode === "short") {
    timer.innerHTML = `0${TIMER.SHORTBREAK}:00`;
  } else {
    timer.innerHTML = `${TIMER.LONGBREAK}:00`;
  }
}

function pomodoro() {
  function setTimer() {
    if (timer.dataset.mode === "pomodoro") {
      seconds = TIMER.POMODORO * 60;
    } else if (timer.dataset.mode === "short") {
      seconds = TIMER.SHORTBREAK * 60;
    } else {
      seconds = TIMER.LONGBREAK * 60;
    }
  }

  if (mainButton.classList.contains("fa-play")) {
    mainButton.classList.replace("fa-play", "fa-stop");
    mainButton.dataset.paused = "false";

    setTimer();

    interval = setInterval(() => {
      let timeRemaining =
        ("0" + Math.floor(seconds / 60)).slice(-2) +
        ":" +
        ("0" + (seconds % 60)).slice(-2);
      timer.innerHTML = timeRemaining;
      document.title = `${timeRemaining} - ${
        timer.dataset.mode === "pomodoro" ? "Work" : "Break"
      }`;

      if (mainButton.dataset.paused === "true" || seconds === 0) {
        clearInterval(interval);
      }
      seconds--;
    }, 1000);
  } else {
    mainButton.classList.replace("fa-stop", "fa-play");
    mainButton.dataset.paused = "true";
  }
}

mainButton.addEventListener("click", pomodoro);
modeButtons.addEventListener("click", changeMode);

*/
var start = document.getElementById('start');
var stop = document.getElementById('stop');
var reset = document.getElementById('reset');

var wm = document.getElementById('w_minutes');
var ws = document.getElementById('w_seconds');

var bm = document.getElementById('b_minutes');
var bs = document.getElementById('b_seconds');

//store a reference to a timer variable
var startTimer;

start.addEventListener('click', function(){
    if(startTimer === undefined){
        startTimer = setInterval(timer, 1000)
    } else {
        alert("Timer is already running");
    }
})

reset.addEventListener('click', function(){
    wm.innerText = 25;
    ws.innerText = "00";

    bm.innerText = 5;
    bs.innerText = "00";

    document.getElementById('counter').innerText = 0;
    stopInterval()
    startTimer = undefined;
})

stop.addEventListener('click', function(){
    stopInterval()
    startTimer = undefined;
})


//Start Timer Function
function timer(){
    //Work Timer Countdown
    if(ws.innerText != 0){
        ws.innerText--;
    } else if(wm.innerText != 0 && ws.innerText == 0){
        ws.innerText = 59;
        wm.innerText--;
    }

    //Break Timer Countdown
    if(wm.innerText == 0 && ws.innerText == 0){
        if(bs.innerText != 0){
            bs.innerText--;
        } else if(bm.innerText != 0 && bs.innerText == 0){
            bs.innerText = 59;
            bm.innerText--;
        }
    }

    //Increment Counter by one if one full cycle is completed
    if(wm.innerText == 0 && ws.innerText == 0 && bm.innerText == 0 && bs.innerText == 0){
        wm.innerText = 25;
        ws.innerText = "00";

        bm.innerText = 5;
        bs.innerText = "00";

        document.getElementById('counter').innerText++;
    }
}

//Stop Timer Function
function stopInterval(){
    clearInterval(startTimer);
}




