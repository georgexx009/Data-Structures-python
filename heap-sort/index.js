const leftFunc = i => i * 2 + 1;
const rightFunc = i => i * 2 + 2;

function swap(arr, a, b) {
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}

const maxHeapify = (arr, i, length) => {
  let l = leftFunc(i);
  let r = rightFunc(i);
  let largest = i;

  if (l < length && arr[l] > arr[largest]) {
    largest = l;
  }
  if (r < length && arr[r] > arr[largest]) {
    largest = r;
  }
  if (largest !== i) {
    swap(arr, i, largest);
    maxHeapify(arr, largest, length);
  }
};

function buildMaxHeap(arr) {
  for (let i = Math.floor(arr.length - 1 / 2); i >= 0; i--) {
    maxHeapify(arr, i, arr.length);
  }
}

function heapSort(arr) {
  buildMaxHeap(arr);

  for (let i = arr.length - 1; i > 0; i--) {
    swap(arr, 0, i);
    maxHeapify(arr, 0, i);
  }
}

const array3 = [6, 5, 4, 3, 2, 1, 4, 8, 10, 34];
heapSort(array3);
console.log(array3);
