# Open Addressing


class HashMap:
    def __init__(self, arrayLength):
        self.arrayLength = arrayLength
        self.array = [None for el in range(arrayLength)]

    # division method
    # linear probing for collision
    def hashFunction(self, key, collisionCount):
        return (sum(key.encode()) + collisionCount) % self.arrayLength

    def compress(self, hashCode):
        return hashCode % self.arrayLength

    def assign(self, key, value):
        collisionCount = 0
        while True:
            hashResult = self.hashFunction(key, collisionCount)
            currentVal = self.array[hashResult]
            if not currentVal or currentVal[0] == key:
                self.array[hashResult] = [key, value]
                return
            collisionCount += 1

            if collisionCount >= self.arrayLength:
                print("hash table full")
                return

    def retrieve(self, key):
			collisionCounter = 0
			while True:
				hashResult = self.hashFunction(key, collisionCounter)
				hashValue = self.array[hashResult]
				if hashValue[0] == key:
					return hashValue[1]
				if not hashValue:					
					return "empty"
				collisionCounter += 1

				if collisionCounter >= self.arrayLength:
					print("empty")
					return
				





hm = HashMap(3)
hm.assign("key", "value")
hm.assign("dos", "value")
hm.assign("tres", "value")

print(hm.array)
