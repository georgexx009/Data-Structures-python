class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_begin(self, new_node):
        new_node.set_next_node(self.head)
        self.head = new_node

    def add_end(self, new_node):
        current_node = self.head
        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def reverse(self):
        before = None
        current = self.head
        after = self.head
        while current:
            after = after.get_next_node()
            current.set_next_node(before)
            before = current
            current = after
        self.head = before

    def __iter__(self):
        current = self.head
        while current:
            yield current.get_value()
            current = current.get_next_node()
