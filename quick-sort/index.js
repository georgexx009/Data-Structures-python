function swap(arr, idx1, idx2) {
  let temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

function quickSort(arr, start, end) {
  if (start >= end) {
    return;
  }

  //let pivotIdx = Math.floor(Math.random() * end) + start;
  let pivotIdx = end;
  let pivotValue = arr[pivotIdx];

  swap(arr, end, pivotIdx);
  let midPointer = start;

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

const arr1 = [6, 5, 4, 3, 2, 1];
quickSort(arr1, 0, arr1.length - 1);
console.log(arr1);

//console.log(Math.floor(Math.random() * 5) + 1);
