function countOccurrences(arr, val) {
    return arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
}