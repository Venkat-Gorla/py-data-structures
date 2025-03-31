# Check if all leaves are at same level

# Given a Binary Tree, check if all leaves are at same level or not.

#         12
#         /
#       5
#     /   \
#    3     9
#   /      /
#  1      2
#  Leaves are at same level

from node import Node
from bfs_utils import bfs_levels_generator

# solution
# can use bfs levels generator
def is_same_leaf_level(root):
    leaf_level = -1
    current_level = 0
    for level in bfs_levels_generator(root):
        for node in level:
            if node.is_leaf():
                if leaf_level == -1:
                    leaf_level = current_level
                elif leaf_level != current_level:
                    return False
        current_level += 1

    return True

# test code
def _test_same_leaf_level():
    assert is_same_leaf_level(None) == True
    root = _create_test_tree()
    assert is_same_leaf_level(root) == True
    print("All test cases for same leaf level passed!")

def _create_test_tree():
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    root.left.right = Node(9)
    root.left.right.left = Node(2)
    return root

if __name__ == "__main__":
    _test_same_leaf_level()

# output:
# All test cases for same leaf level passed!
