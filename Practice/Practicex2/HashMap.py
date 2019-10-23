from LinkedList import LinkedList
from Node import Node

class HashMap:
    def __init__(self, arraySize):
        self.arraySize = arraySize
        self.array = [LinkedList() for item in range(self.arraySize)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hashCode):
        return hashCode % self.arraySize


    def assign(self, key, value):
        arrayIndex = self.compress(self.hash(key))
        arrayList = self.array[arrayIndex]

        for el in arrayList:
            if key == el[0]:
                el[1] = value
        arrayList.insert_last(Node([key, value]))


    def retrieve(self, key):
        arrayIndex = self.compress(self.hash(key))
        arrayList = self.array[arrayIndex]

        for node in arrayList:
            if node[0] == key:
                return node[1]
        return None

hashMap = HashMap(3)
hashMap.assign('key1', 'value1')
hashMap.assign('key2', 'value2')
hashMap.assign('key3', 'value3')
hashMap.assign('kye4', 'value4')
#hashMap.ite('key4')
hashMap.assign('key4', 'value5')
print(hashMap.retrieve('key1'))
print(hashMap.retrieve('key2'))
print(hashMap.retrieve('key3'))
print(hashMap.retrieve('key4'))
print(hashMap.retrieve('kye4'))
