from getSubStrings import getSubStrings
from checkAnagram import checkAnagram

testWord = "kkkk"

def sherlockAndAnagrams(s):
  subStrings = getSubStrings(s)
  print(subStrings)
  counter = 0

  for i in range(len(subStrings)):
    for j in range(i + 1, len(subStrings)):
      if i != j and checkAnagram(subStrings[i], subStrings[j]):
        counter += 1        
  return counter

result = sherlockAndAnagrams(testWord)
print(result)