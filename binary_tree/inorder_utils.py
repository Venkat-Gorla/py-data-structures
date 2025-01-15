
# some reusable code for inorder traversal

# inorder traversal using generator and yield
def inorder_generator(root):
    current = root
    nodeStack = []

    while current or nodeStack:
        while current:
            nodeStack.append(current)
            current = current.left

        current = nodeStack.pop()
        yield current
        current = current.right

