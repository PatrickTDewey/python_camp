let date = document.querySelector('.date-on-load');

window.onload = (e) => {
    date.innerHTML = new Date();
}