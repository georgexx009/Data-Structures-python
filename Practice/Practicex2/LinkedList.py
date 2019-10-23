from Node import Node

class LinkedList:
	def __init__(self, value=None):
		self.head_node = value


	def insert_last(self, node):
		new_node = node

		if not self.head_node:
			self.head_node = new_node
			return

		next_node = self.head_node

		while next_node.get_next_node() != None:
			next_node = next_node.get_next_node()
		next_node.set_next_node(new_node)


	#remove_multiple_nodes
	def __iter__(self):
		current_node = self.head_node
		while current_node:
			yield current_node.value
			current_node = current_node.get_next_node()
