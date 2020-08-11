def getSubStrings(str1):
  result = []
  for i in range(len(str1)):
    for j in range(i + 1, len(str1)+1):
      result.append(str1[i:j])

  return result

