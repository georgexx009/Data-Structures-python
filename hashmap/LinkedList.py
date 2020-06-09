# working


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def insert_last(self, value):
        new_node = Node(value)
        next_node = self.head_node
        while next_node.get_next_node() != None:
            next_node = next_node.get_next_node()
        next_node.set_next_node(new_node)

    def stringfy(self):
        string = ""
        next_node = self.head_node
        while next_node != None:
            string += str(next_node.get_value()) + "\n"
            next_node = next_node.get_next_node()
        return string

    # remove_multiple_nodes
    def __iter__(self):
        current_node = self.head_node
        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next_node()

