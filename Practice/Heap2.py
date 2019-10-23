class HeapMin:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2
    def right_child_idx(self, idx):
        return idx * 2 + 1
    def left_child_idx(self, idx):
        return idx * 2

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()


    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx):
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            idx = self.parent_idx(idx)


    def retrieve_min(self):
        pass

    def heapify_down(self):
        pass

    def get_smaller_child_idx(self):
        pass

heap = HeapMin()
heap.add(3)
heap.add(2)
heap.add(5)
heap.add(6)
heap.add(1)
print(heap.heap_list)
