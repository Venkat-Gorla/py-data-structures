
# given a list of strings, find and group anagrams.
# you should return list<list<string>> where each inner list represents a group of anagrams.
# for example: "abc" and "bca" are anagrams and should be grouped inside the same inner list.

def find_anagrams(input_list):
    anagram_groups = {}

    for word in input_list:
        sorted_word = ''.join(sorted(word))
        anagram_groups.setdefault(sorted_word, []).append(word)

    # starting with python 3.7, values will be returned in order of insertion,
    # so the result will be deterministic for validation inside the calling code
    return list(anagram_groups.values())

def test_find_anagrams():
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert find_anagrams(input_list) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    input_list = ["abc", "bca", "cab"]
    assert find_anagrams(input_list) == [['abc', 'bca', 'cab']]

    print('All anagram tests passed')

if __name__ == '__main__':
    test_find_anagrams()

# output
# All anagram tests passed

