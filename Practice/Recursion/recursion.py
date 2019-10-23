def sumToOne(n):
	result = 1
	callStack = []

	while n != 1:
		executionContext = {"n_value": n}
		callStack.append(executionContext)
		n -= 1
		print(callStack)
	print("Base Case Reached")

	while len(callStack) != 0:
		returnValue = callStack.pop()
		print("remain call stack" + str(callStack))		
		print("returned value: " + str(returnValue["n_value"]))
		result += returnValue["n_value"]
		print("----------------")

	return result, callStack 

#sumToOne(4)


def powerSet(myList):
	powerSetSize = 2**len(myList)
	result = []
	
	for bit in range(0, powerSetSize):
		subSet = []
		for binaryDigit in range(0, len(myList)):
			print("BinaryDigit: {0}".format(binaryDigit))
			print("1 << binaryDigit: {0}".format(1 << binaryDigit))
			print("bit: {0}".format(bit))
			print("bit & (1 << binaryDigit): {0}".format(bit & (1 << binaryDigit)))
			if (bit & (1 << binaryDigit)) > 0:
				subSet.append(myList[binaryDigit])
		result.append(subSet)
		print("------------------------------------")
	
	return result

#print(powerSet(['one', 'two', 'three']))


def powerSet2(myList):
	#Base Case: an empty list
	if len(myList) == 0:
		return[[]]

	# recursive step: subsets without first element
	powerSetWithoutFirst = powerSet2(myList[1:])

	# subset with first element
	withFirst = [ [myList[0]] + rest for rest in powerSetWithoutFirst]
	print("withFirst: {0}".format(withFirst))
	print("powerSet: {0}".format(powerSetWithoutFirst))
	return withFirst + powerSetWithoutFirst

print(powerSet2(['one', 'two', 'three']))

#123-(23)//23-(3)//