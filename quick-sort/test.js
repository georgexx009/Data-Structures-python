function swap(arr, idx1, idx2) {
  let temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

function quickSort(arr, start, end) {
  if (start >= end) {
    return;
  }

  let pivotValue = arr[end];
  let midPointer = start;

  //not include last one, because is the pivot
  for (let i = start; i < end; i++) {
    if (arr[i] < pivotValue) {
      swap(arr, i, midPointer);
      midPointer++;
    }
  }

  swap(arr, midPointer, end);

  quickSort(arr, start, midPointer - 1);
  quickSort(arr, midPointer + 1, end);
}

const arr1 = [4, 8, 17, 14, 10, 19, 2, 6, 9, 15];
quickSort(arr1, 0, arr1.length - 1);
console.log(arr1);
