from LinkedList import LinkedList

ll = LinkedList(1)
ll.insert_last(2)
ll.insert_last(3)
ll.insert_last(4)
ll.insert_last(4)
ll.insert_last(5)
ll.insert_beginning(0)
ll.remove_node2(4)

print(ll.stringfy())
