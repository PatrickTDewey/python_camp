let boxes = document.getElementsByClassName('box');
console.log(boxes);

function addColor(arr) {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
        let mySplit = arr[i].className.split(' ');
        console.log(mySplit);
        arr[i].style.background = mySplit[1];
    }
}

console.log(addColor(boxes));