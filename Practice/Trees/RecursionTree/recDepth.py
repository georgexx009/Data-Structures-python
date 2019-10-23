def rec_depth(tree):
    if not tree:
        return 0

    left_depth = rec_depth(tree["left_child"])
    right_depth = rec_depth(tree["right_child"])

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1
