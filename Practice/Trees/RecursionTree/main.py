from buildTree import build_tree
from recDepth import rec_depth
from iteDepth import ite_depth



tree1 = build_tree([1, 2, 3])
print(tree1)

print(rec_depth(tree1))
print(ite_depth(tree1))


builded_tree = {
    'data': 2,
    'left_child': {
        'data': 1,
        'left_child': None,
        'right_child': None
    },
    'right_child': {
        'data': 3,
        'left_child': None,
        'right_child': None
    }
}


two_level_tree = {
    "data": 6,
    "left_child":{
        "data": 2
    }
}
