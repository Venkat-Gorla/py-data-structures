
# Binary Tree to Binary Search Tree Conversion

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from node import Node # binary tree Node
from inorder_utils import inorder_generator

# the structure of the converted bst should be identical to the input binary tree
# we can swap the node values where necessary
# can use inorder generator and do selection sort

def get_tree_len(root):
    tree_len = 0
    for _ in inorder_generator(root):
        tree_len += 1
    return tree_len

def convert_to_bst(root):
    remaining_nodes = get_tree_len(root)

    while remaining_nodes > 1:
        gen = inorder_generator(root)
        max_node_in_pass = None
        current_node = None

        for _ in range(remaining_nodes):
            current_node = next(gen)
            if max_node_in_pass is None or current_node.data > max_node_in_pass.data:
                max_node_in_pass = current_node

        if current_node is not max_node_in_pass:
            current_node.data, max_node_in_pass.data = max_node_in_pass.data, current_node.data

        remaining_nodes -= 1

def print_inorder(root):
    for node in inorder_generator(root):
        print(node.data, end=" ")
    print()

def test_convert_to_bst():
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    print("Input binary tree inorder:")
    print_inorder(root)

    convert_to_bst(root)
    print("\nConverted BST inorder:")
    print_inorder(root)

if __name__ == '__main__':
    test_convert_to_bst()

# output:
# Input binary tree inorder:
# 20 30 10 15 5

# Converted BST inorder:
# 5 10 15 20 30

