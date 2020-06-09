function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const middle = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, middle));
  const right = mergeSort(arr.slice(middle, arr.length));
  return merge(left, right);
}

function merge(left, right) {
  let result = [];

  while (left.length > 0 && right.length > 0) {
    if (left[0] < right[0]) {
      result.push(left[0]);
      left.splice(0, 1);
    } else {
      result.push(right[0]);
      right.splice(0, 1);
    }
  }

  if (left.length > 0) {
    result = [...result, ...left];
  } else if (right.length > 0) {
    result = [...result, ...right];
  }

  return result;
}

const result = mergeSort([6, 2, 3, 5, 9, 1]);
console.log(result);
