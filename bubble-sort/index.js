function swap(arr, a, b) {
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}

function bubbleSort(arr) {
  let counter = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      counter++;
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
      }
    }
  }
  return counter;
}

const array1 = [6, 5, 4, 3, 2, 1];
const iterations = bubbleSort(array1);
console.log(array1);
console.log(iterations);

function bubbleSort2(arr) {
  let counter = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1 - i; j++) {
      counter++;
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
      }
    }
  }
  return counter;
}

const array2 = [6, 5, 4, 3, 2, 1];
const iterations2 = bubbleSort2(array2);
console.log(array2);
console.log(iterations2);
