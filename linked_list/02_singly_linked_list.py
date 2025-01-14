
# given a singly linked list (sll), reverse it between a pair of start and end indexes, inclusive.
# the list is 0 indexed and you can assume 'start' and 'end' indexes are valid.
# example:
# 1->2->3->4->5 and reverse_between(1, 3) should yield
# 1->4->3->2->5
# 1->2->3->4->5 and reverse_between(0, 4) should yield
# 5->4->3->2->1
# 1->2->3->4->5 and reverse_between(0, 0) should yield
# 1->2->3->4->5
# The list should be modified in-place with pointer manipulation
# 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # this can be simplified with a tail, but not using it
    # since our focus is the reverse_between implementation
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

    # solution function
    def reverse_between(self, start_index, end_index):
        if self.head is None or start_index == end_index:
            return

        dummy_node = Node(0)
        dummy_node.next = self.head

        prefix = dummy_node
        for _ in range(start_index):
            prefix = prefix.next

        previous = None
        current = prefix.next
        for _ in range(end_index - start_index + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first_reversed_node = prefix.next
        prefix.next = previous
        first_reversed_node.next = current

        if start_index == 0:
            self.head = previous

    # useful for test cases
    def from_list(self, data):
        for item in data:
            self.append(item)

    def to_list(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

def test_list_creation():
    sll = SinglyLinkedList()
    sll.from_list([1, 2, 3, 4, 5])
    assert sll.to_list() == [1, 2, 3, 4, 5]
    print("List creation test passed")

def test_list_reverse_between():
    def build_and_reverse_between(lst, start, end):
        sll = SinglyLinkedList()
        sll.from_list(lst)
        sll.reverse_between(start, end)
        return sll.to_list()

    # Test cases
    assert build_and_reverse_between([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
    assert build_and_reverse_between([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
    assert build_and_reverse_between([1, 2, 3, 4, 5], 0, 0) == [1, 2, 3, 4, 5]
    assert build_and_reverse_between([1, 2, 3, 4, 5], 0, 2) == [3, 2, 1, 4, 5]
    assert build_and_reverse_between([], 0, 0) == []
    print("List reverse between tests passed")

if __name__ == '__main__':
    test_list_creation()
    test_list_reverse_between()

# output
# List creation test passed
# List reverse between tests passed

