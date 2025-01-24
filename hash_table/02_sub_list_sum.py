
# given a list of numbers and a target number, check if there is a contiguous sub-list
# whose sum is equal to the target

def get_sub_list_with_sum(numbers, target):
    """
    Given a list of numbers and a target number, check if there is a sub-list
    whose sum is equal to the target.

    :param numbers: list of numbers
    :param target: target number
    :return: list of indices of the sub-list whose sum is equal to the target,
    [] if no such sub-list exists
    """
    # by doing this we don't need to special case for current_sum == target
    sum_index_table = {0: -1}

    current_sum = 0
    for number_index, number in enumerate(numbers):
        current_sum += number
        find_sum = current_sum - target
        if find_sum in sum_index_table:
            return [sum_index_table[find_sum] + 1, number_index]
        sum_index_table[current_sum] = number_index

    return []

def test_get_sub_list_with_sum():
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 12) == [2, 4]
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 15) == [0, 4]
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 14) == [1, 4]
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 7) == [2, 3]
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 2) == [1, 1]
    assert get_sub_list_with_sum([1, 2, 3, 4, 5], 0) == []

    print("get_sub_list_with_sum tests passed")

if __name__ == "__main__":
    test_get_sub_list_with_sum()

# output
# get_sub_list_with_sum tests passed

