#taco cat

def check_palindrome(phrase):
	#delete spaces, will return the new string
	#strings are immutable
	phrase = phrase.replace(" ", "")
	j = len(phrase) - 1 #pointer to the end
	
	for i in range(len(phrase)//2): #avoid floats
		if phrase[i] != phrase[j - i]:
			return False
	return True

test1 = "taco cat"
test2 = "kayak"
test3 = "racecar"
test4 = "a"
test5 = "ufo tofu"
print(check_palindrome(test1))
print(check_palindrome(test2))
print(check_palindrome(test3))
print(check_palindrome(test4))
print(check_palindrome(test5))
    