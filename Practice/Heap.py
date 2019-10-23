class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2
    def left_child_idx(self, idx):
        return idx * 2
    def right_child_idx(self, idx):
        return idx * 2 + 1


    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()


    def heapify_up(self):
        idx = self.count #last node added
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            idx = self.parent_idx(idx)



    def retrieve_min(self):
        if self.count == 0:
            return None

        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return min


    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)

            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            if parent > child:
                self.heap_list[smaller_child_idx] = parent
                self.heap_list[idx] = child

            idx = smaller_child_idx


    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                return self.right_child_idx(idx)
            else:
                return self.left_child_idx(idx)

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count




#-----------------------------------------------------------------------------
heap = MinHeap()
heap.add(3)
heap.add(2)
heap.add(5)
heap.add(6)
heap.add(1)
heap.add(4)
heap.add(8)
print(heap.heap_list)
heap.retrieve_min()
print(heap.heap_list)
