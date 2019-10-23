class HashMap:
    def __init__(self, arraySize):
        self.arraySize = arraySize
        self.array = [None for element in range(arraySize)]

    def hash(self, key, collisionCount):
        return sum(key.encode()) + collisionCount

    def compress(self, hashCode):
        return hashCode % self.arraySize

    def assign(self, key, value):
        collisionCount = 0
        while True:
            arrayIndex = self.compress(self.hash(key, collisionCount))
            currentValue = self.array[arrayIndex]
            if not currentValue or currentValue[0] == key:
                self.array[arrayIndex] = [key, value]
                return
            collisionCount += 1

            if collisionCount >= self.arraySize:
                print('array full')
                return

    def retrieve(self, key):
        collisionCount = 0
        while True:
            arrayIndex = self.compress(self.hash(key, collisionCount))
            currentValue = self.array[arrayIndex]
            if not currentValue:
                return None
            if currentValue[0] == key:
                return currentValue[1]
            collisionCount += 1
            if collisionCount >= self.arraySize:
                return None

hm = HashMap(3)
hm.assign('eykrwer', 'value2')
hm.assign('ekyfds', 'value3')
hm.assign('eyk2', 'value4')
hm.assign('eyk2das', 'value4')
print(hm.retrieve('key'))
print(hm.array)
