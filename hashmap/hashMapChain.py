# working

from LinkedList import LinkedList
from LinkedList import Node


class HashMap:
    def __init__(self, mapSize):
        self.mapSize = mapSize
        self.array = [LinkedList() for el in range(mapSize)]

    def hashFunc(self, key):
        return sum(key.encode()) % self.mapSize

    def add(self, key, value):
        hashResult = self.hashFunc(key)
        currentList = self.array[hashResult]

        for el in currentList:
            if key == el[0]:
                el[1] = value
                return
        currentList.insert_last(Node([key, value]))

    def retrieve(self, key):
        hashResult = self.hashFunc(key)
        currentList = self.array[hashResult]

        for el in currentList:
            if not el:
                return
            if el[0] == key:
                print(el[1])
                return
        print("not found")


hm = HashMap(4)
hm.add("key", "value")
print(hm.array)

