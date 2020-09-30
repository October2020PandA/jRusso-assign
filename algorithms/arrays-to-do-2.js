var testArr = [5, 2, 4, 9, 1];

// Min to Front
function minToFront(arr) {
    var min = arr[0];
    var pos = 0;
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min =  arr[i];
            pos = i;
        }
    }
    for (var i = pos; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = min;
    return;
}

// minToFront(testArr);
// console.log(testArr);