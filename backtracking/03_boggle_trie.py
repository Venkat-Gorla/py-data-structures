
# boggle solution using Trie
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../trie'))
from trie import Trie

def create_trie():
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    # basic validation
    assert trie.search("GEEKS")

    return trie

# to calculate neighbors of current cell
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

def word_helper(
    boggle, row, col, path, all_words,
    current_node # caller has to ensure this is not None
):
    num_rows, num_cols = len(boggle), len(boggle[0])

    original_value = boggle[row][col]
    boggle[row][col] = 0
    path.append(original_value)

    current_word = ''.join(path)
    if current_node.is_end_of_word:
        all_words.append(current_word)

    # recursively check all neighbors of current cell
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < num_rows and 0 <= nc < num_cols and boggle[nr][nc] != 0:
            next_letter = boggle[nr][nc]
            if next_letter in current_node.children:
                word_helper(
                    boggle, nr, nc, path, all_words,
                    current_node.children[next_letter]
                )

    boggle[row][col] = original_value
    path.pop()

def test_boggle_word_helper():
    trie = create_trie()
    
    boggle = [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
    ]

    path = []
    all_words = []
    for row in range(len(boggle)):
        for col in range(len(boggle[0])):
            if boggle[row][col] in trie.root.children:
                word_helper(
                    boggle, row, col, path, all_words, 
                    trie.root.children[boggle[row][col]]
                )

    print("Found the following words in the boggle:")
    print(all_words)

if __name__ == '__main__':
    test_boggle_word_helper()

# output
# Found the following words in the boggle:
# ['GEEKS', 'QUIZ']

