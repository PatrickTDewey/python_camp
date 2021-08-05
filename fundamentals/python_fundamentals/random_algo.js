// let pala = "aabbbbaa"
// let notPala = "bbaabb"
// let daddyo = "whats up daddy-o"
// function isPalendrom(string){
//     for (let i = 0; i < string.length / 2 ; i++) {
//         if (string[i] != string[string.length -i -1]) {
//             return false
//         }
//     }
//     return true;
// }
// console.log(isPalendrom(pala));
// console.log(isPalendrom(notPala));

// function countSubstring(string){
//     let list = [];
//     let palaList = [];
//     for (let i = 0; i < string.length; i++) {
//         let temp = ''
//         start = i;
//         for (let j = start; j < string.length ; j++) {
//             temp += string[j]
//         }
//         if (isPalendrom(temp)) {
//             list.push(temp)

//         }


//     }
//     console.log(list);

// }

// countSubstring(pala)
// countSubstring(daddyo)

/*
    Given a sorted array of page numbers where a term appears,
    produce an index string.

    Consecutive pages should form ranges separated by a hyphen

    BONUS: Only use the hyphen IF there are 3 or more consecutive pages.

    EXAMPLE:

    var input = [1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27];

    var output = "1, 5-10, 14, 22-25, 27";

    var input2 = [2, 3, 4, 7, 8, 10, 12, 14, 15, 16, 17];

    BASIC:
    var output2 = "2-4, 7-8, 10, 12, 14-17";
    BONUS:
    var output2 = "2-4, 7, 8, 10, 12, 14-17";
*/
let myBook = [1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27];
var input2 = [2, 3, 4, 7, 8, 10, 12, 14, 15, 16, 17];
let vinnysEdgeCase = [];
function bookIndex(pages) {
    let new_string = '';
    let count = 0;
    for (let i = 0; i < pages.length; i++) {
        new_string += pages[i];
        while (pages[i] + 1 == pages[i + 1]) {
            i++;
            count++;
        }
        if (count == 1) {
            i--;
            new_string += ', ';
        }
        else if (count != 0) {

            new_string += '-' + (pages[i]);
            if (i != pages.length - 1) {
                new_string += ', ';
            }
        }
        else if (i != pages.length - 1) {
            new_string += ', ';
        }
        count = 0;
    }
    return new_string;
}
console.log(bookIndex(myBook));
console.log(bookIndex(input2));
console.log(bookIndex(vinnysEdgeCase));
// Vinny G , Spencer R, Kalyb, Lai L, Ryan P, Patrick D