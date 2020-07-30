#open addressing
class HashMap:
  def __init__(self, size):
    self.size = size
    self.array = [None] * size

  def hash_code(self, key, col_num):
    # division method with collision resolution by open addressing     
    return (sum(key.encode()) + col_num) % self.size 

  def insert(self, key, value):
    new_el = (key, value) # tuple key-value
    col_num = 0  # collision counter
    
    # finding right slot
    while True:            
      hash_val = self.hash_code(key, col_num)
      print(hash_val)
      current_el = self.array[hash_val]
      if current_el == None or current_el[0] == key:  # not assign yet
        self.array[hash_val] = new_el
        return
      else:
        col_num += 1
        if col_num > self.size:
          print("hasmap full")
          return

  def delete(self, key):    
    col_num = 0

    while True:
      hash_val = self.hash_code(key, col_num)
      current_el = self.array[hash_val]
      if current_el == None:
        print("value does not exist")
        return None
      elif current_el[0] == key:
        self.array[hash_val] = None
      else:
        col_num += 1
        if col_num > self.size:
          print("value does not exist")
          return



hm = HashMap(6)
hm.insert("key1", "value")
hm.insert("kye1", "value")
hm.insert("yek1", "value")
hm.insert("yek3", "value")
hm.insert("yek4", "value")
hm.insert("yek7", "value")

hm.delete("das")
hm.delete("yek7")
hm.insert("das", "value")
print(hm.array)