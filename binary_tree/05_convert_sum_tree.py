# Convert a given tree to its Sum Tree

# Given a Binary Tree where each node has positive and negative values, convert it to a tree where each node contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

# For example, the following tree

#                   10
#                /      \
#              -2        6
#             /   \     /  \
#            8    -4   7    5
# should be changed to

#                  20(4-2+12+6)
#                /      \
# 	        4(8-4)      12(7+5)
#            /   \      /  \
#           0     0    0    0

from node import Node

# solution function
def convert_to_sum_tree(root):
    if root is None:
        return 0

    sub_tree_sum = convert_to_sum_tree(root.left) + convert_to_sum_tree(root.right)

    # python style, multi variable assignment in one go
    old_value, root.data = root.data, sub_tree_sum
    return old_value + root.data

def create_test_tree():
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)
    return root

def test_sum_tree_conversion():
    root = create_test_tree()
    convert_to_sum_tree(root)
    assert root.data == 20
    assert root.left.data == 4
    assert root.right.data == 12
    assert root.left.left.data == 0
    assert root.left.right.data == 0
    assert root.right.left.data == 0
    assert root.right.right.data == 0
    print("All tests for Sum tree conversion passed")

if __name__ == '__main__':
    test_sum_tree_conversion()

# output
# All tests for Sum tree conversion passed
