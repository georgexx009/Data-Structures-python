from LinkedList import LinkedList
from Node import Node

class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [LinkedList() for i in range(self.size)]


    def hash(self, key):
        return sum(key.encode())
    def compress(self, hash_code):
        return hash_code % self.size


    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            print(item[0])
            #if key == item[0]:
                #node[1] = value
        list_at_array.insert_last(payload)

    def assign2(self, key, value):
      array_index = self.compress(self.hash(key))
      payload = Node([key, value])
      list_at_array = self.array[array_index]
      for item in list_at_array:
          if key == item[0]:
              item[1] = value
              return
      list_at_array.insert(payload)


    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                return item[1]
        return None

hm = HashMap(4)
hm.assign2("one", 1)
#hm.retrieve("one")
