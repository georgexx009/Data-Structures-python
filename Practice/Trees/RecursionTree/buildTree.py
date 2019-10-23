def build_tree(list):
	if not list:
		return

	mid_idx = len(list) // 2
	mid_value = list[mid_idx]

	treeNode = { "data": mid_value }
	treeNode["left_child"] = build_tree(list[:mid_idx])
	treeNode["right_child"] = build_tree(list[mid_idx + 1:])

	return treeNode