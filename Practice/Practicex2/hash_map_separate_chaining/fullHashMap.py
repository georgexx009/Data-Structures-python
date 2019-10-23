class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    def getNextNode(self):
        return self.nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def assign(self, newNode):
        if not self.head:
            self.head = newNode
