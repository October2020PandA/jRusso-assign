var testArr = [1, 3, 5, 5, 8]

// Push Front
function pushFront(arr, val) {
    for (var i = arr.length; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = val;
    return arr;
}

// var newArr = pushFront(testArr, 3);
// console.log(newArr);

// Pop Front
function popFront(arr) {
    var output = arr[0];
    delete arr[0];
    return output;
}

// var testValue = popFront(testArr);
// console.log(testValue);

// Insert At
function insertAt(arr, pos, val) {
    for (var i = arr.length; i >= 0; i--) {
        if (i <= pos) {
            arr[i] = val;
            return;
        }
        arr[i] = arr[i - 1];
    }
    return;
}

// insertAt(testArr, 0, 3);
// console.log(testArr);

// Remove At
function removeAt(arr, pos) {
    var output = '';
    for (var i = arr.length; i >= 0; i--) {
        if (i <= pos) {
            output = arr[i];
            delete arr[i];
            break;
        }
    }
    return output;
}

// console.log(removeAt(testArr, 2));

// Swap Pairs
function swapPairs(arr) {
    var holder = '';
    for (var i = 1; i < arr.length; i = i + 2) {
        holder = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = holder;
    }
    return;
}

// swapPairs(testArr);
// console.log(testArr);

// Remove Duplicates
function removeDuplicates(arr) {
    for (var i = 0; i < arr.length - 1; i++) {
        if (arr[i] == arr[i + 1]) {
            delete arr[i + 1];
        }
    }
    return;
}

// removeDuplicates(testArr);
// console.log(testArr);