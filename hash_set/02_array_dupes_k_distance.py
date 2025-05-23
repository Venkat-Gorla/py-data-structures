# Check if a given array contains duplicate elements within k distance from each other

# Given an unsorted array that may contain duplicates. Also given a number k which is smaller 
# than the size of the array.
# Write a function that returns true if the array contains duplicates within k distance.

# Examples:

# Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
# Output: false
# All duplicates are more than k distance away.

# Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
# Output: true
# 1 is repeated at distance 3.

# solution function
# we will use a hash set to store the most recent k elements of the array
# and check if the current element is already in the set. If it is, we return true.
def check_duplicates(arr, k):
    hash_set = set()

    for index, element in enumerate(arr):
        if element in hash_set:
            return True

        hash_set.add(element)

        if index >= k:
            hash_set.remove(arr[index - k])

    return False

# Test cases
def test_check_duplicates():
    assert check_duplicates([1, 2, 3, 4, 1, 2, 3, 4], 3) == False
    assert check_duplicates([1, 2, 3, 1, 4, 5], 3) == True
    assert check_duplicates([1, 2, 3, 1], 0) == False
    assert check_duplicates([1, 2, 1, 4], 2) == True
    assert check_duplicates([], 0) == False
    assert check_duplicates([1], 0) == False
    assert check_duplicates([10, 5, 3, 4, 3, 5, 6], 3) == True

if __name__ == "__main__":
    test_check_duplicates()
    print("All test cases for check_duplicates() passed!")

# output:
# All test cases for check_duplicates() passed!
