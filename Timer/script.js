const semicircles = document.querySelectorAll('.semicircle');
const timer = document.querySelector('.timer');


//inoput
const hr = 0;
const min = 0;
const sec = 10;


const hours = hr * 3600000;
const minutes = min * 60000;
const seconds = sec * 1000;
const setTime = hours + minutes + seconds;
const startTime = Date.now()
const futureTime = startTime + setTime;

const timerLoop = setInterval(countDownTimer)
countDownTimer();

function countDownTimer() {
    const currentTime = Date.now();
    const remainingTime = futureTime - currentTime;
    const angle = (remainingTime / setTime) * 360;
    //progress
    if(angle > 180) {
        semicircles[2].style.display = 'none' ;
        semicircles[0].style.transform = `rotate(180deg)` ;
        semicircles[1].style.transform = `rotate(${angle}deg)` ;
    } else {
        semicircles[2].style.display = 'block';
        semicircles[0].style.transform = `rotate(${angle}deg)` ;
        semicircles[1].style.transform = `rotate(${angle}deg)` ;
    }

    // timer
    const hrs = Math.floor((remainingTime / (1000 * 60 * 60)) % 24 ).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    const mins = Math.floor((remainingTime / (1000 * 60)) % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    const secs = Math.floor((remainingTime / (1000)) % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false});
    timer.innerHTML = `
    <div class="hrs">${hrs}</div>
    <div class="colon1">:</div>
    <div class="mins">${mins}</div>
    <div class="colon2">:</div>
    <div class="secs">${secs}</div>
    `

    //red circle 5 sec
    if(remainingTime < 6000) {
        semicircles[0].style.backgroundColor = "red";
        semicircles[1].style.backgroundColor = "red";
        timer.style.color = "red";
    }

    //end  
    if (remainingTime < 0) {
        clearInterval(timerLoop);
        timer.innerHTML = `
    <div class="hrs">00</div>
    <div class="colon1">:</div>
    <div class="mins">00</div>
    <div class="colon2">:</div>
    <div class="secs">00</div>
    `
    }
}