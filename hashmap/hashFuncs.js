/*
  using the JavaScript function charCodeAt() to return a character’s ASCII value 
  after multiplying the ASCII value by a multiplier H, which in this case, is an odd prime 37. 
  And the reason to choose 37 being, by some empirical research, 
  if we take over 50,000 English words (formed as the union of the word 
  lists provided in two variants of Unix), using the constants 31, 33, 37, 39, and 41 
  will produce less than 7 collisions in each case, while creating a hasing function.
*/

function stringToHash(string) {
  var hash = 0;

  if (string.length == 0) return hash;

  for (i = 0; i < string.length; i++) {
    char = string.charCodeAt(i); //gets the ansii value or utf - 8 character code value.
    hash = (hash << 5) - hash + char;
    hash = hash & hash; // Convert to 32bit integer
  }

  return hash;
}

function hashMod(str, tableLength) {
  let key = 0;
  const prime = 37;

  const length = str.length;
  for (let i = 0; i < length; i++) {
    key += prime * key + str.charCodeAt(i);
  }

  key %= tableLength;
  if (key < 1) {
    tableLength - 1;
  }

  return parseInt(key);
}

module.exports = { hashMod, stringToHash };
