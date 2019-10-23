from Node import Node

class LinkedList:
	def __init__(self, value=None):
		self.head_node = Node(value)

	def get_head_node(self):
		return self.head_node

	def insert_beginning(self, value):
		new_node = Node(value)
		new_node.set_next_node(self.head_node)
		self.head_node = new_node

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

	def remove_node(self, remove_value):
		if self.head_node.get_value() == remove_value:
			self.head_node = self.head_node.get_next_node()
		else:
			current_node = self.head_node
			while current_node.get_next_node() != None:
				next_node = current_node.get_next_node()
				if next_node.get_value() == remove_value:
					current_node.set_next_node(next_node.get_next_node())
					break
				else:
					current_node = next_node

	#remove_multiple_nodes
	def __iter__(self):
		current_node = self.head_node
		while current_node is not None:
			yield current_node.get_value()
			current_node = current_node.get_next_node()


ll = LinkedList("First")
ll.insert_last("second")
ll.insert_last("third")
for item in ll:
	print(item)
