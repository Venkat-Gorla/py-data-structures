
# In place conversion of sorted doubly linked list (dll) to balanced binary search tree (bst)

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from node import Node
from inorder_utils import inorder_generator

# sample for testing
root = Node(1)
print('Inorder traversal using generator:')
for current in inorder_generator(root):
    print(current.data, end=' ')

