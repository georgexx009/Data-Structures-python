#enqueue, dequeue, peek
#head, tail, opt max size
from Node import Node
class Queue:

    def __init__(self, max_size=None):
        self.max_size = max_size
        self.tail = None
        self.head = None
        self.size = 0

    def stringify(self):
        string = "Head \n"
        current_node = self.head
        while current_node is not None:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string + "Tail"

    def enqueue(self, value):
        if has_space():
            new_node = Node(value)
            if self.size == 0:
                self.tail = new_node
                self.head = new_node
            else:
                self.tail.set_next_node(new_node)
                self.tail = new_node
            self.size += 1
        else:
            print("This queue is full")

    def dequeue(self):
        if self.size == 0:
            return "The queue is empty"
        else:
            node_remove = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return node_remove.get_value()

    def peek(self):
        if self.size == 0:
            return "The queue is empty"
        else:
            return self.head.get_value()

    def has_space(self):
        if self.max_size:
            return self.max_size > self.size
        return True
