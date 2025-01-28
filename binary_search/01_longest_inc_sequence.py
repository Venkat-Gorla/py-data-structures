
# we will explore an alternate solution to the longest increasing subsequence problem 
# without using DP; the alternate solution is greedy approach + binary search

import bisect

def longest_increasing_subsequence(numbers):
    subsequence = [] # will be maintained in sorted order

    for number in numbers:
        if not subsequence or number > subsequence[-1]:
            subsequence.append(number)
        else:
            # replace the element at the index with the current number;
            # this is the greedy part of the solution
            index = bisect.bisect_left(subsequence, number)
            subsequence[index] = number

    return len(subsequence)

def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1

    print("longest_increasing_subsequence tests passed")

if __name__ == "__main__":
    test_longest_increasing_subsequence()

# output
# longest_increasing_subsequence tests passed

