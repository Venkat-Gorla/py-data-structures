
# Inorder Successor in Binary Search Tree
# unlike Binary tree, this is different, we don't need to do a complete tree traversal
# it can be done using a simple while loop and a binary search for the desired key

from bst_utils import create_bst

def find_inorder_successor(root, key):
    successor = None
    current = root
    while current:
        if key < current.data:
            successor = current
            current = current.left
        elif key > current.data:
            current = current.right
        else:
            break

    if not current: # search key not found
        return None

    if current.right:
        successor = current.right
        while successor.left:
            successor = successor.left

    return successor

def test_find_inorder_successor():
    bst_keys = [20, 8, 22, 4, 12, 10, 14]
    root = create_bst(bst_keys)
    assert find_inorder_successor(root, 4).data == 8

    sorted_keys = sorted(bst_keys)
    sorted_keys.append(None)
    for i in range(len(sorted_keys) - 1):
        successor = find_inorder_successor(root, sorted_keys[i])
        assert (successor and successor.data) == sorted_keys[i + 1]

    print("Bst inorder successor tests passed")

if __name__ == '__main__':
    test_find_inorder_successor()

# output
# Bst inorder successor tests passed

