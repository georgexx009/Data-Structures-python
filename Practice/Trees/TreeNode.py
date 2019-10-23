class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        if type(child) is TreeNode:
            self.children.append(child)

    def remove_child(self, remove_child):
        if type(remove_child) is TreeNode:
            self.children = [node for node in self.children if node.value is not remove_child.value]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

    def traverse2(self):
        print(self.value)
        for node in self.children:
            print(node.value)

root = TreeNode("root")
root.add_child(TreeNode("child1"))
root.add_child(TreeNode("child2"))
child3 = TreeNode("child3")
root.add_child(child3)
child3.add_child(TreeNode("child3child"))
child3.add_child(TreeNode("child3child2"))
root.traverse()
#child3.remove_child(TreeNode("child3child2"))
root.remove_child("child2")
root.traverse()
