class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# some helper functions for testing
def create_list(input):
    if not input:
        return None

    head = Node(input[0])
    current = head
    for i in input[1:]:
        current.next = Node(i)
        current = current.next

    return head

def is_sorted(head):
    if not head or not head.next:
        return True

    current = head
    while current.next:
        if current.data > current.next.data:
            return False
        current = current.next

    return True

def get_list_len(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

# create and return a python list from the linked list data
def get_list_data(head):
    output = []
    current = head
    while current:
        output.append(current.data)
        current = current.next
    return output
