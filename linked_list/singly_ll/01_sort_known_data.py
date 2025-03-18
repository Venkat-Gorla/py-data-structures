# given a singly linked list containing only 0's, 1's and 2's, sort the list in ascending order
# Time complexity: O(n)
# Space complexity: O(1)

from node import *

# solution function
# we will solve this problem using pointer manipulation and not data reassignment
# in place sort function, "head" should Not be referenced after calling this function
def sort_list_known_data(head):
    head_zero = None
    head_one = None
    head_two = None

    current = head
    while current:
        next_node = current.next
        if current.data == 0:
            current.next = head_zero
            head_zero = current
        elif current.data == 1:
            current.next = head_one
            head_one = current
        else:
            current.next = head_two
            head_two = current

        current = next_node

    # merge the three lists
    # note that any of the three lists can be empty
    # by creating a dummy node, we can avoid the need to check if a list is empty
    dummy = Node(0)
    dummy.next = head_zero
    last_node = get_last_node(dummy)
    last_node.next = head_one
    last_node = get_last_node(last_node)
    last_node.next = head_two

    return dummy.next

# caller has to ensure head is Not None
def get_last_node(head):
    current = head
    while current.next:
        current = current.next
    return current

def _test_sort_list_known_data(input):
    head = create_list(input)
    input_len = get_list_len(head) # store list len, since head will be modified

    sorted_head = sort_list_known_data(head)
    assert input_len == get_list_len(sorted_head)
    assert is_sorted(sorted_head)

def _test_cases():
    _test_sort_list_known_data([])
    _test_sort_list_known_data([0, 0, 0])
    _test_sort_list_known_data([1, 1, 1])
    _test_sort_list_known_data([2, 2, 2])
    _test_sort_list_known_data([0, 1, 2])
    _test_sort_list_known_data([2, 1, 0])
    _test_sort_list_known_data([0, 2, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2])
    print("All tests for sort list with known data passed")

if __name__ == '__main__':
    _test_cases()

# output:
# All tests for sort list with known data passed
