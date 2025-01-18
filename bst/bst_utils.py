
# some helper functions and related code for bst creation, manipulation etc.

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from node import Node, print_tree

# recursive function to insert a new node into bst
def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)

    return root

def create_bst(bst_keys):
    root = None
    for key in bst_keys:
        root = insert(root, key)
    return root

def test_insert():
    bst_keys = [2, 1, 3, 4]
    root = create_bst(bst_keys)

    print('printing created bst')
    print_tree(root)

if __name__ == '__main__':
    test_insert()

# output: 
# printing created bst
# -->2 (root)
#    |-->1 (L)
#    |-->3 (R)
#    |   |-->4 (R)

