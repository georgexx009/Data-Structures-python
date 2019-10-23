from Node import Node

class Stack:
    def __init__(self, limit=10):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def stringfy(self):
        if not self.is_empty():
            current_node = self.top_item
            str = ""
            while current_node is not None:
                str += current_node.get_value() + "\n"
                current_node = current_node.get_next_node()
        else:
            str = "Is still empty"
        return str

    def push(self, value):
        new_item = Node(value)
        if self.has_space():
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
            print("Adding {} to the stack".format(value))
        else:
            print("No more space")

    def pop(self):
        if not self.is_empty():
            remove_value = self.top_item
            self.top_item = remove_value.get_next_node()
            self.size -= 1
            print("Removing {} from stack".format(remove_value.get_value()))
            return remove_value.get_value()
        else:
            print("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value
        return "The stack is empty"

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
