class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head_node = None):
        self.head_node = Node(head_node)

    def insert(self, value):
        current_node = self.head_node

        if not current_node:
            self.head_node = value

        while current_node:
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(value)
                #print("set " + current_node.get_next_node().get_value())
            current_node = next_node

    def insert_last(self, value):
        next_node = self.head_node
        new_node = Node(value)
        while next_node.get_next_node() != None:
            next_node = next_node.get_next_node()
        next_node.set_next_node(new_node)

    def __iter__(self):
        current_node = self.head_node
        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next_node()

ll = LinkedList("first")
ll.insert_last("two")
ll.insert_last("three")

for item in ll:
    print(item)
