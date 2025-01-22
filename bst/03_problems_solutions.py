
# Here we will explore a collection of common bst problems and their solutions

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from inorder_utils import inorder_generator
from bst_utils import create_bst

#----------------------------------------
# Print Common Nodes in Two Binary Search Trees i.e. nodes with common data values

# the inorder generator comes handy, given the sorted nature of bst when doing inorder traversal,
# we can simply do a merge sort kind of algorithm to find nodes with common values

# solution function
def find_common_nodes(root1, root2):
    print("Printing common nodes of given bst's:")
    first_gen = inorder_generator(root1)
    second_gen = inorder_generator(root2)

    first_node = next(first_gen, None)
    second_node = next(second_gen, None)

    while first_node is not None and second_node is not None:
        if first_node.data == second_node.data:
            print(first_node.data, end=" ")
            first_node = next(first_gen, None)
            second_node = next(second_gen, None)
        elif first_node.data < second_node.data:
            first_node = next(first_gen, None)
        else:
            second_node = next(second_gen, None)
    print()

def test_find_common_nodes():
    first_list = [5, 1, 10, 0, 4, 7, 9]
    second_list = [10, 7, 20, 4, 9]
    root1 = create_bst(first_list)
    root2 = create_bst(second_list)
    find_common_nodes(root1, root2)

if __name__ == '__main__':
    test_find_common_nodes()

# output:
# Printing common nodes of given bst's:
# 4 7 9 10

#----------------------------------------
# in place convert BST to sorted DLL i.e. doubly linked list

# should be able to use inorder generator
# dll node will also use tree node structure (left and right pointers)
# solution function
def convert_bst_to_dll(root):
    """
    In place convert bst to sorted dll

    Args:
        root: root of the bst

    Returns:
        head of the sorted dll
    """
    if root is None:
        return None

    gen = inorder_generator(root)
    head_node = next(gen, None)
    prev_node = head_node
    for node in gen:
        prev_node.right = node
        node.left = prev_node
        prev_node = node

    return head_node

def test_convert_bst_to_dll():
    bst_list = [5, 1, 10, 0, 4, 7, 9]
    print(f"\nPrinting keys list from which bst will be created: {bst_list}")
    root = create_bst(bst_list)
    head_node = convert_bst_to_dll(root)
    print("Printing sorted dll after conversion from bst:")
    while head_node is not None:
        print(head_node.data, end=" ")
        head_node = head_node.right
    print()

if __name__ == '__main__':
    test_convert_bst_to_dll()

# output:
# Printing keys list from which bst will be created: [5, 1, 10, 0, 4, 7, 9]
# Printing sorted dll after conversion from bst:
# 0 1 4 5 7 9 10

