
# In place conversion of sorted doubly linked list (dll) to balanced binary search tree (bst)

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../binary_tree'))
from node import Node, print_tree # binary tree Node
from inorder_utils import inorder_generator

class DoublyLinkedList:
    """
    A class representing a doubly linked list. The Node structure will be that of
    binary tree however.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        """
        Add a node to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
        self.length += 1

    def reset_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    # solution function
    def convert_to_balanced_bst(self):
        """
        Convert the doubly linked list to a balanced binary search tree.
        Dll head and tail attributes are updated to None and length is set to 0.
        The list is expected to be sorted, this function will not do sorting.

        Returns: root of the balanced binary search tree
        """
        def convert_helper(num_nodes, head_ref):
            if num_nodes <= 0:
                return None

            left_tree = convert_helper(num_nodes // 2, head_ref)

            root = Node(head_ref[0].data)
            head_ref[0] = head_ref[0].right

            right_tree = convert_helper(num_nodes - num_nodes // 2 - 1, head_ref)

            root.left = left_tree
            root.right = right_tree

            return root

        root = convert_helper(self.length, [self.head])
        self.reset_list()
        return root

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.right
        return result

    def from_list(self, lst):
        for item in lst:
            self.append(item)

def build_dll(lst):
    dll = DoublyLinkedList()
    dll.from_list(lst)
    assert dll.length == len(lst)
    return dll

def test_dll_build():
    assert build_dll([1, 2, 3]).to_list() == [1, 2, 3]
    print('dll build test passed')

def test_convert_to_balanced_bst():
    input_list = [1, 2, 3, 4, 5, 6, 7]
    input_dll = build_dll(input_list)
    assert input_dll.to_list() == input_list

    bst_root = input_dll.convert_to_balanced_bst()
    assert input_dll.head is None
    assert input_dll.tail is None
    assert input_dll.length == 0

    inorder_list = [node.data for node in inorder_generator(bst_root)]
    assert inorder_list == input_list

    print('printing converted tree structure')
    print_tree(bst_root)
    print('convert to balanced bst test passed')

if __name__ == '__main__':
    test_dll_build()
    test_convert_to_balanced_bst()

# output
# dll build test passed
# printing converted tree structure
# -->4 (root)
#    |-->2 (L)
#    |   |-->1 (L)
#    |   |-->3 (R)
#    |-->6 (R)
#    |   |-->5 (L)
#    |   |-->7 (R)
# convert to balanced bst test passed

