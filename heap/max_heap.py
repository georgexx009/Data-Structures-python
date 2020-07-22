class MaxHeap:
  def __init__(self, initial_size=0, initial_heap=[None]):
    self.size = initial_size  #will help to track heap size
    self.heap = initial_heap

  def parent_idx(self, idx):
    return idx // 2
    
  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def insert(self, new_element):
    self.size += 1
    self.heap.append(new_element)
    current_el = self.size
    parent = self.parent_idx(current_el)
    while parent > 0:
      self.heapify_up(current_el)
      current_el = parent
      parent = self.parent_idx(current_el)

  def heapify_up(self, el_idx):  #the el is the current element on the swapping
    parent_val = self.heap[self.parent_idx(el_idx)]
    current_val = self.heap[el_idx]

    if parent_val < current_val:
      self.heap[self.parent_idx(el_idx)] = current_val
      self.heap[el_idx] = parent_val
  
  def max_retrieve(self):
    self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
    self.size -= 1
    max_val = self.heap.pop()
    self.heapify_down(1)
    
  def heapify_down(self, current_idx):
    #check if childs are not out of scope
    #check which child is larger to switch places
    #if none of them, we finish
    #repeat this process with child switched

    current_val = self.heap[current_idx]
    max_idx = current_idx

    left_child_idx = self.left_child_idx(current_idx)
    right_child_idx = self.right_child_idx(current_idx)

    if left_child_idx <= self.size and current_val < self.heap[left_child_idx]:
      max_idx = left_child_idx
    if right_child_idx <= self.size and current_val < self.heap[right_child_idx]:
      max_idx = right_child_idx

    if max_idx == current_idx:
      return
    else:
      self.heap[current_idx], self.heap[max_idx] = self.heap[max_idx], self.heap[current_idx]
      self.heapify_down(max_idx)
    

    






exampleHeap = [None, 6, 4, 5, 3, 2, 0, 1]
mh = MaxHeap(7, exampleHeap)
print(mh.heap)
mh.max_retrieve()
print(mh.heap)
  