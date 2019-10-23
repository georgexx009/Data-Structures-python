class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent(self, idx):
        return idx // 2
    def left(self, idx):
        return idx * 2
    def right(self, idx):
        return idx * 2 + 1

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        parent_idx = self.parent(self.count)
        current_idx = self.count
        while parent_idx <= 0:
            parent = self.heap_list[parent_idx]
            child = self.heap_list[current_idx]
            if parent > child:
                self.heap_list[parent_idx], self.heap_list[current_idx] = child, parent
            current_idx = parent_idx
            parent_idx = self.parent(current_idx)

    def retrieve_min(self):
        if self.count == 0:
            return None

        self.heap_list[1], self.heap_list[self.count] = self.heap_list[self.count], self.heap_list[1]
        min = self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return min

    def heapify_down(self):
        current = 1
        while self.left(current) <= self.count:
            child_idx = get_smaller_child_idx(current)
            parent = self.heap_list[current]
            child = self.heap_list[child_idx]
            if parent > child:
                self.heap_list[current], self.heap_list[child_idx] = child, parent 
            current = child_idx

    def get_smaller_child_idx(self, idx):
        right = right(idx)
        left = left(idx)

        if right > self.count:
            return left
        if self.heap_list[right] > self.heap_list[left]:
            return left
        else:
            return right













#preseve end
