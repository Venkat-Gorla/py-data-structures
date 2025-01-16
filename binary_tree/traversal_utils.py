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

def test_postorder_generator():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('postorder traversal:')
    for node in postorder_generator(root):
        print(node.data, end=' ')
    print()

if __name__ == '__main__':
    test_postorder_generator()

# output:
# postorder traversal:
# 4 5 2 3 1

