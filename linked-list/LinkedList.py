class Node:
  def __init__(self, value, pointer):
    self.value = value
    self.pointer = pointer
  
  def setPointer(self, newPointer):
    self.pointer = newPointer

class LinkedList:
  def __init__(self, head):
    self.head = Node(head, None)

  def iterateToLastNode(self):
    currentNode = self.head
    while currentNode.pointer != None:
      currentNode = currentNode.pointer
    return currentNode

  def addToTail(self, newValue):
    newNode = Node(newValue, None)
    if self.head is None:
      self.head = newNode
      return
    
    lastNode = self.iterateToLastNode()    
    lastNode.pointer = newNode

  def searchValue(self, target):
    currentNode = self.head
    while currentNode != None:
      if currentNode.value == target:
        return True
      currentNode = currentNode.pointer
    return False

  def deleteElement(self, target):
    if self.head == None:
      return False

    if self.head.value == target:
      self.head = self.head.pointer
      return True
    prevNode = self.head      
    currentNode = self.head.pointer    
    while currentNode != None:
      if currentNode.value == target:
        prevNode.setPointer(currentNode.pointer)
        return True
      prevNode = currentNode
      currentNode = currentNode.pointer
    return False

  def getSize(self):    
    if self.head == None:
      return 0
    counter = 0
    currentNode = self.head
    while currentNode != None:
      counter += 1
      currentNode = currentNode.pointer
    return counter

  def reverseList(self):
    if self.head is None:
      return None
    currentNode = self.head
    prevNode = currentNode
    nextNode = self.head.pointer
    currentNode.setPointer(None)
    while nextNode != None:
      currentNode = nextNode
      nextNode = nextNode.pointer
      currentNode.setPointer(prevNode)
      prevNode = currentNode        
    self.head = currentNode

  def printLinkedList(self):
    if self.head is None:
      print('empty list')
      return None
    
    currentNode = self.head
    print('Head: {}'.format(currentNode.value))
    while currentNode.pointer != None:
      currentNode = currentNode.pointer
      print(currentNode.value)


ll = LinkedList(0)
ll.deleteElement(0)
ll.printLinkedList()
ll.addToTail(1)
ll.addToTail(2)
ll.addToTail(3)
ll.addToTail(4)

# ll.printLinkedList()
# ll.reverseList()
# ll.printLinkedList()
print(ll.deleteElement(0))
ll.addToTail(0)
ll.printLinkedList()
print(ll.getSize())

  