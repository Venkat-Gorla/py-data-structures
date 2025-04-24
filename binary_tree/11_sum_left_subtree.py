# Change a Binary Tree so that every node stores sum of all nodes in left subtree

# Given a Binary Tree, change the value in each node to sum of all the values in the nodes in the left subtree including its own.

# Input : 
#      1
#    /   \
#  2      3

# Output :
#     3
#   /   \
#  2     3

# Input
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# Output:
#       12
#      / \
#     6   3
#    / \   \
#   4   5   6

from node import Node
from inorder_utils import inorder_generator

# recursive solution
# every node must update it's data with the sum of it's left subtree and 
# return total sum to it's parent
def sum_left_subtree(root):
    if root is None:
        return 0

    left_sum = sum_left_subtree(root.left)
    right_sum = sum_left_subtree(root.right)

    root.data += left_sum
    return root.data + right_sum

# test related code
def _test_sum_left_subtree():
    root = _create_test_tree()
    sum_left_subtree(root)
    print('Inorder traversal of the modified tree is')
    for current in inorder_generator(root):
        print(current.data, end=' ')
    print()

def _create_test_tree():
    # Let us construct the below tree
    #             1
    #            / \
    #           2   3
    #          / \   \
    #         4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root

if __name__ == '__main__':
    _test_sum_left_subtree()

# Output:
# Inorder traversal of the modified tree is
# 4 6 5 12 3 6
