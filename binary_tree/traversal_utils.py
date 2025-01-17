# some reusable code for binary tree traversals

from node import Node

# postorder generator function
def postorder_generator(root):
    if root is None:
        return

    current = root
    node_stack = []
    last_visited = None

    while current or node_stack:
        if current:
            node_stack.append(current)
            current = current.left
        else:
            peek_node = node_stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                yield peek_node
                last_visited = node_stack.pop()

# pending: 
# refactor common code after testing
def postorder_paths_generator(root):
    """
    In addition to generating the nodes in postorder, it also returns
    the connecting path from the root to the current node

    Returns: tuple of (node_path, current_node)
    """
    if root is None:
        return

    current = root
    node_stack = []
    last_visited = None

    while current or node_stack:
        if current:
            node_stack.append(current)
            current = current.left
        else:
            peek_node = node_stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                yield list(node_stack), peek_node
                last_visited = node_stack.pop()

def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

def test_postorder_generator():
    root = create_tree()

    print('postorder traversal:')
    for node in postorder_generator(root):
        print(node.data, end=' ')
    print()

def test_postorder_paths_generator():
    root = create_tree()

    print('\npostorder traversal with paths:')
    for node_path, node in postorder_paths_generator(root):
        print(*(node.data for node in node_path), end='---')
        print(node.data)
    print()

if __name__ == '__main__':
    test_postorder_generator()
    test_postorder_paths_generator()

# output:
# postorder traversal:
# 4 5 2 3 1

# postorder traversal with paths:
# 1 2 4---4
# 1 2 5---5
# 1 2---2
# 1 3---3
# 1---1

