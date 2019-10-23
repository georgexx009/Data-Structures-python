from Node import Node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def add_end(self, value):
        new_node = Node(value)
        current_node = self.head
        #make a modification here
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node
        current_node.set_next_node(new_node)

    def multiple_remove(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                
