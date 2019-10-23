class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def set_next(self, new_node):
        self.next_node = new_node

    def get_next(self):
        return self.next_node


class LinkedList:
    def __init__(self, head):
        self.head = Node(head)

    def get_head(self):
        return self.head

    def add_final(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def stringfy(self):
        string = ""
        current_node = self.head
        while current_node is not None:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next()
        return string

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next()


ll = LinkedList(1)
ll.add_final(2)
ll.add_final(3)
ll.add_final(4)
print(ll.stringfy())
