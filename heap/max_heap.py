class MaxHeap:
  def __init__(self, initialSize=0, initialHeap=[None]):
    self.size = initialSize  #will help to track heap size
    self.heap = initialHeap

  def parentIdx(self, idx):
    return idx//2

  def insert(self, newElement):
    self.size += 1
    self.heap.append(newElement)
    currentEl = self.size
    parent = self.parentIdx(currentEl)
    while parent > 0:
      self.heapify_up(currentEl)
      currentEl = parent
      parent = self.parentIdx(currentEl)

  def heapify_up(self, elIdx):  #the el is the current element on the swapping
    parentVal = self.heap[self.parentIdx(elIdx)]
    currentVal = self.heap[elIdx]

    if parentVal < currentVal:
      self.heap[self.parentIdx(elIdx)] = currentVal
      self.heap[elIdx] = parentVal




exampleHeap = [None, 6, 4, 5, 3, 2, 0, 1]
mh = MaxHeap(7, exampleHeap)
print(mh.heap)
mh.insert(7)
print(mh.heap)
  