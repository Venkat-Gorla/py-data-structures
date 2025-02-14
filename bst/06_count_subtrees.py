
# Given a Binary Search Tree (BST) of integer values and a range [low, high], 
# return count of nodes where all the nodes under that node (or subtree rooted 
# with that node) lie in the given range.

from bst_utils import create_bst

# recursive helper function, for every node we will return a "flag, count" tuple
# that will indicate if the current subtree satisfies the range condition and the
# number of nodes in the range
def count_bst_subtrees(root, min_val, max_val):
    if not root:
        return True, 0

    left_flag, left_count = count_bst_subtrees(root.left, min_val, max_val)
    right_flag, right_count = count_bst_subtrees(root.right, min_val, max_val)

    if left_flag and right_flag and min_val <= root.data <= max_val:
        return True, 1 + left_count + right_count
    else:
        return False, left_count + right_count

def count_bst_subtrees_in_range(root, min_val, max_val):
    root_flag, root_count = count_bst_subtrees(root, min_val, max_val)
    return root_count

def test_count_bst_subtrees_in_range():
    bst_keys = [10, 5, 50, 1, 40, 100]
    root = create_bst(bst_keys)
    assert count_bst_subtrees_in_range(root, 5, 45) == 1
    assert count_bst_subtrees_in_range(root, 1, 45) == 3
    assert count_bst_subtrees_in_range(root, 1, 100) == 6
    assert count_bst_subtrees_in_range(root, 0, 100) == 6
    print('All bst subtrees in range tests passed')

if __name__ == '__main__':
    test_count_bst_subtrees_in_range()

# output:
# All bst subtrees in range tests passed

