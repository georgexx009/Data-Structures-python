#open addressing
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(self.array_size)]

#------------------------------------------------------------------------

    def hash(self, key, count_collision = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collision

    def compress(self, hash_code):
        return hash_code % self.array_size

#------------------------------------------------------------------------

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        #collision!
        
