
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

