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
# end function

# test code
def _test_same_leaf_level():
    _test_success_case()
    _test_failure_case()
    print("All test cases for same leaf level passed!")

def _test_success_case():
    assert is_same_leaf_level(None) == True
    root = _create_success_tree()
    assert is_same_leaf_level(root) == True
    print("Success test case passed")

def _create_success_tree():
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    root.left.right = Node(9)
    root.left.right.left = Node(2)
    return root

def _test_failure_case():
    root = _create_failure_tree()
    assert is_same_leaf_level(root) == False
    print("Failure test case passed")

def _create_failure_tree():
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    root.right = Node(9)
    root.right.left = Node(2)
    root.right.right = Node(4)
    return root

if __name__ == "__main__":
    _test_same_leaf_level()

# output:
# Success test case passed
# Failure test case passed
# All test cases for same leaf level passed!
