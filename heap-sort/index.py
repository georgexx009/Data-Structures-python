class Heap:
    def __init__(self):
        self.heapList = [None]
        self.count = 0
        
    def parentIdx(self, idx):
        return idx // 2
    def leftChildIdx(self, idx):
        return idx * 2
    def rightChildIdx(self, idx):
        return idx * 2 + 1
        
    #retrieve and add
    
    #check if is empty
    #get min element idx 1
    #change the first one with the last one
    #pop last one
    #discount
    #heapify down
    
    def retrieveMin(self):
        if self.count == 0:
            return None
        
        min = self.heapList[1]
        self.heapList[1] = self.heapList[self.count]
        self.count =- 1
        self.heapList.pop()
        self.heapifyDown()
        return min
        
    #append it
    #count increment
    #heapify up
    
    def add(self, element):
        self.count += 1
        self.heapList.append(element)
        self.heapifyUp()
        
    #create var with last index to work with it
    #loop while a parent exists
    #if the parent is higher, switch
    #update the idx with parent idx
    
    #check every node until root
        
    def heapifyUp(self):
        idx = self.count
        
        while self.parentIdx(idx) > 0:
            if self.heapList[self.parentIdx(idx)] > self.heapList[idx]:
                temp = self.heapList[self.parentIdx(idx)]
                self.heapList[self.parentIdx(idx)] = self.heapList[idx]
                self.heapList[idx] = temp
            idx = self.parentIdx(idx)
            
    #check if right child exist, if not return left one
    #else get childs values and see which is smaller
            
    def getSmallerChildIdx(self, idx):
        if self.rightChildIdx(idx) > self.count:
            return self.leftChildIdx(idx)
        else:
            leftChild = self.heapList[self.leftChildIdx(idx)]
            rightChild = self.heapList[self.rightChildIdx(idx)]
            if leftChild > rightChild:
                return self.rightChildIdx(idx)
            else:
                return self.leftChildIdx(idx)
            
    #create var with root index node
    #loop while a child exists
    #get smaller child
    #if parent is higher switch
    #update index var and let them run until last child
            
    def heapifyDown(self):
        idx = 1
        
        while self.leftChildIdx(idx) <= self.count:
            smallerChildIdx = self.getSmallerChildIdx(idx)
            if self.heapList[idx] > self.heapList[smallerChildIdx]:
                temp = self.heapList[smallerChildIdx]
                self.heapList[smallerChildIdx] = self.heapList[idx]
                self.heapList[idx] = temp
            idx = smallerChildIdx
            
heap = Heap()
heap.add(1)
heap.add(10)
heap.add(6)
heap.add(4)
print(heap.heapList)
print(heap.retrieveMin())
print(heap.heapList)
            
#dont heapify down
            
            
            
            