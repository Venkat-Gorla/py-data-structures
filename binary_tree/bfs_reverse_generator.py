# alternate solution for reverse bfs generator using default dictionary and
# recursive dfs function

from node import Node
from collections import defaultdict

def bfs_reverse_generator(root):
    if not root:
        return

    output_levels = defaultdict(list)

    # dfs helper function, internal
    def dfs(current, level):
        if not current:
            return
        output_levels[level].append(current)
        dfs(current.left, level + 1)
        dfs(current.right, level + 1)

    dfs(root, 0)

    for level in range(len(output_levels) - 1, -1, -1):
        yield from output_levels[level]

def _create_test_tree():
    # create a binary tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root

def _test_reverse_bfs_generator():
    root = _create_test_tree()

    print('Reverse BFS traversal of the binary tree is:')
    for current in bfs_reverse_generator(root):
        print(current.data, end=' ')
    print()

if __name__ == '__main__':
    _test_reverse_bfs_generator()

# Output:
# Reverse BFS traversal of the binary tree is:
# 4 5 6 2 3 1
