function swap(arr, idx1, idx2) {
  let temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

function quickSort(arr, start, end) {
  //if is equal means only one element which means is sorted
  if (start < end) {
    const m = partition(arr, start, end);
    quickSort(arr, start, m - 1);
    quickSort(arr, m + 1, end);
  }
}

function partition(arr, start, end) {
  //const pivot = arr[end];

  const pivotIdx = Math.floor(Math.random() * end) + start;
  console.log(pivotIdx);
  const pivot = arr[pivotIdx];
  swap(arr, end, pivotIdx);

  let mid = start;
  for (let i = start; i < end; i++) {
    counter++;
    if (arr[i] < pivot) {
      swap(arr, mid, i);
      mid++;
    }
  }
  swap(arr, mid, end);
  return mid;
}
let counter = 0;
const arr1 = [6, 8, 4, 5, 3];
//const arr1 = [4, 8, 17, 14, 10, 19];
quickSort(arr1, 0, arr1.length - 1);
console.log(arr1);
console.log(counter);
