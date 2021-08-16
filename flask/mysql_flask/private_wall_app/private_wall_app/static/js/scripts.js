console.log('hi');

function updateTime(){
    let currentTime = new Date();
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();
    if (minutes < 10){
        minutes = "0" + minutes
    }
    if (seconds < 10){
        seconds = "0" + seconds
    }
    if (hours > 11) {
        seconds += " PM";
    } else {
        seconds += ' AM';
    }
    let time_string = `${hours}:${minutes}:${seconds}`;
    document.querySelector('.date').innerHTML = time_string;
    setTimeout(updateTime, 1000);
}
updateTime();