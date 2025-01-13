
# Trie implementation for word storage and lookup

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]

        current.is_end_of_word = True

    def _traverse(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return None
            current = current.children[letter]
        return current

    def search(self, word):
        current = self._traverse(word)
        return current is not None and current.is_end_of_word

def test_trie_search():
    trie = Trie()
    dictionary = ["hello", "world", "trie", "structure", "python"]
    for word in dictionary:
        trie.insert(word)

    assert trie.search("hello")
    assert trie.search("trie")
    assert trie.search("tree") is False

    print("Trie search test cases passed")

if __name__ == "__main__":
    test_trie_search()

