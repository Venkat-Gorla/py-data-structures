
# Given an unsorted array of integers, write a function that finds the length of the longest Consecutive Sequence (i.e., a sequence of integers in which each element is one greater than the previous element).
# Output: an integer representing the length of the longest consecutive sequence
# Example:

# Input: int[] nums = [100, 4, 200, 1, 3, 2]

# Output: 4

# Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.

# Approach:
# - in python the built-in set uses hashing to provide O(1) access time
# - copy the input array into a set.
# - for every input element in the array, check if it is the start of a sequence, it will be
#   the first if (number - 1) is Not present in the set.
# - calculate current sequence length and update max length.

def longest_consecutive_sequence(numbers):
    input_set = set(numbers)
    max_sequence_length = 0

    for number in numbers:
        if number - 1 in input_set:
            continue

        # current number is the start of a sequence
        current_sequence_length = 1
        current_number = number
        while current_number + 1 in input_set:
            current_sequence_length += 1
            current_number += 1

        max_sequence_length = max(max_sequence_length, current_sequence_length)

    return max_sequence_length

def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_sequence([1, 2, 0, 1]) == 3
    assert longest_consecutive_sequence([1, 2, 0, 1, 2, 3]) == 4

    print("longest_consecutive_sequence tests passed")

if __name__ == "__main__":
    test_longest_consecutive_sequence()

# output
# longest_consecutive_sequence tests passed

