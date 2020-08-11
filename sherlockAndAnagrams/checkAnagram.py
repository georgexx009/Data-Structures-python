def checkAnagram(str1, str2):
  if len(str1) != len(str2):
    return False

  str1 = ''.join(sorted(str1))
  str2 = ''.join(sorted(str2))

  return str1 == str2