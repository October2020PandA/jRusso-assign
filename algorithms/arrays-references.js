var testArr = [5, 2, 4, 9, 1];

// Reverse
function reverse(arr) {
    for (var i = 0; i < Math.floor(arr.length / 2); i++) {
        [arr[i], arr[arr.length - i - 1]] = [arr[arr.length - i - 1], arr[i]]
    }
    return;
}

// reverse(testArr);
// console.log(testArr);

// Rotate
function rotate(arr, shiftBy) {
    
}