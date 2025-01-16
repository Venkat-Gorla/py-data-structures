
# Two nodes of a BST are swapped, correct the BST

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from node import Node # binary tree Node
from inorder_utils import inorder_generator

# we will use inorder generator to solve this problem
# if the swapped nodes are next to one another, you will have one violation;
# if not, you will have two violations
def correct_bst_nodes(root):
    first = None
    second = None
    third = None
    previous = None

    for current in inorder_generator(root):
        if previous and previous.data > current.data:
            if not first:
                first = previous
                second = current
            else:
                third = current
        previous = current

    if third:
        first.data, third.data = third.data, first.data
    elif first and second:
        first.data, second.data = second.data, first.data

def print_inorder(root):
    for node in inorder_generator(root):
        print(node.data, end=' ')
    print()

def test_correct_bst_nodes(root):
    print('printing inorder traversal before and after correction')
    print_inorder(root)
    correct_bst_nodes(root)
    print_inorder(root)

def test_bst_conversion():
    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(12)
    root.right.left = Node(7)
    test_correct_bst_nodes(root)

    # test case where swapped nodes are next to one another
    root = Node(3)
    root.left = Node(1)
    root.right = Node(2)
    print()
    test_correct_bst_nodes(root)

if __name__ == '__main__':
    test_bst_conversion()

# output:
# printing inorder traversal before and after correction
# 1 10 3 6 7 2 12
# 1 2 3 6 7 10 12

# printing inorder traversal before and after correction
# 1 3 2
# 1 2 3

