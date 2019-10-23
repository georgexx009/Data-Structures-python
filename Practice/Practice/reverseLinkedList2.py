class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def get_value(self):
        return self.value
    def set_next_node(self, new_node):
        self.next_node = new_node
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self, head):
        self.head = Node(head)

    def insert_last(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def stringfy(self):
        string = ""
        current_node = self.head
        while current_node is not None:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield str(current_node.get_value())
            current_node = current_node.get_next_node()

    def reverseList(self):
        previous = None
        current = self.head
        next_node = self.head
        while current is not None:
            next_node = next_node.get_next_node()
            current.set_next_node(previous)
            previous = current
            current = next_node
            #next_node = next_node.get_next_node()
        #self.head = current
        self.head = previous

ll = LinkedList(1)
ll.insert_last(2)
ll.insert_last(3)
ll.insert_last(4)



#print(ll.stringfy())
ll.reverseList()
for i in ll:
    print(i + "r")
