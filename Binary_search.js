function binary_search(arr, item) {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let guess = arr[mid];

        if (guess == item) return mid;

        guess < item ? low = mid + 1 : high = mid - 1;
    }
    return null;
}

// Testing
const sortedList = [...Array(15).keys()];

console.log(binary_search(sortedList, 4));
console.log(binary_search(sortedList, 9));
console.log(binary_search(sortedList, 11));
