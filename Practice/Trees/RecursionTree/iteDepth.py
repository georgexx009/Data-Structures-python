def ite_depth(tree):
    if not tree:
        return 0

    result = 0
    queue = [tree]

    while queue:
        level_count = len(queue)
        for childs in range(0, level_count):
            child = queue.pop(0)
            if "left_child" in child:
                queue.append(child["left_child"])
            if "right_child" in child:
                queue.append(child["right_child"])
            result += 1
            print("result: {0}".format(result))
    return result




two_level_tree = {
"data": 6,
"left_child":
  {"data": 2},
"right_child":
  {"data": 2},
}

print(ite_depth(two_level_tree))
