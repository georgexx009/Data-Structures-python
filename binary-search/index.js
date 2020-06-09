function binarySearch(arr, target) {
  let startIdx = 0;
  let endIdx = arr.length;
  let steps = 0;

  //less equal because it could ends in 1 element to divide
  while (startIdx <= endIdx) {
    //5 - 10, 5+10=15/2=7.5 round down 7
    let middleIdx = Math.floor((startIdx + endIdx) / 2);
    console.log(++steps);

    if (target === arr[middleIdx]) {
      return middleIdx;
    }
    if (target > arr[middleIdx]) {
      startIdx = middleIdx + 1;
    } else {
      endIdx = middleIdx - 1;
    }
  }

  return -1;
}

const array1 = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(binarySearch(array1, 9));
