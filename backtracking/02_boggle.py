
# Given a dictionary, and a M x N board where every cell has one character. 
# Find all possible words that can be formed by a sequence of adjacent characters. 
# Note that we can move to any of 8 adjacent characters, but a word 
# should not have multiple instances of same cell.

# Example:

# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"}
#        boggle[][]   = {{'G','I','Z'},
#                        {'U','E','K'},
#                        {'Q','S','E'}}

# Output:  Following words of dictionary are present
#          GEEKS
#          QUIZ

dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

# to calculate neighbors of current cell
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

def word_helper(boggle, row, col, path, all_words):
    num_rows, num_cols = len(boggle), len(boggle[0])

    original_value = boggle[row][col]
    boggle[row][col] = 0
    path.append(original_value)

    current_word = ''.join(path)
    if current_word in dictionary:
        all_words.append(current_word)

    # recursively check all neighbors of current cell
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < num_rows and 0 <= nc < num_cols and boggle[nr][nc] != 0:
            word_helper(boggle, nr, nc, path, all_words)

    boggle[row][col] = original_value
    path.pop()

def test_boggle_word_helper():
    boggle = [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
    ]

    path = []
    all_words = []
    for row in range(len(boggle)):
        for col in range(len(boggle[0])):
            word_helper(boggle, row, col, path, all_words)

    print("Found the following words in the boggle:")
    print(all_words)

if __name__ == '__main__':
    test_boggle_word_helper()

# output
# Found the following words in the boggle:
# ['GEEKS', 'QUIZ']

