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
    console.log(arr);
    if (shiftBy % arr.length == 0) {
        return;
    }
    shiftBy = shiftBy % arr.length;
    if (shiftBy < 0) {
        shiftBy = arr.length + shiftBy;
    }
    var j = 0, k = 0, l = arr[j], m = '';
    if (arr.length % 2 == 0 && shiftBy % 2 == 0) {
        var j2 = 1, k2 = 0, l2 = arr[j2], m2 = '';
        for (var i = 0; i < arr.length; i = i + 2) {
            k = (j + shiftBy) % arr.length;
            k2 = (j2 + shiftBy) % arr.length;
            m = arr[k];
            m2 = arr[k2];
            arr[k2] = l2;
            arr[k] = l;
            j2 = k2;
            j = k;
            l2 = m2;
            l = m;
        }
    } else {
        for (var i = 0; i < arr.length; i++) {
            k = (j + shiftBy) % arr.length;
            m = arr[k];
            arr[k] = l;
            j = k;
            l = m;
        }
    }
    console.log(arr);
}

// rotate(testArr, 4);

// Filter Range
function filterRange(arr, min, max) {
    for (var i = arr.length - 1; i > -1; i--) {
        if (arr[i] < min) {
            delete arr[i];
            arr.length = arr.length - 1;
        } else if (arr[i] > max) {
            delete arr[i];
            arr.length = arr.length - 1;
        }
    }
}

// filterRange(testArr, 2, 5);
// console.log(testArr);

// Concat
function arrConcat(arr1, arr2) {
    var outputArr = [];
    for (var i = 0; i < arr1.length; i++) {
        outputArr.push(arr1[i]);
    }
    for (var i = 0; i < arr2.length; i++) {
        outputArr.push(arr2[i]);
    }
    return outputArr;
}

// testArr2 = [3, 5, 1];
// concatArr = arrConcat(testArr, testArr2);
// console.log(concatArr);