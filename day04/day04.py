#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2024   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  4  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 2571            |            #
#            |  `-----------'   Part 2: 1992            |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

from collections import namedtuple

Pos = namedtuple('Pos', ['row', 'col'])

class WordSearch():
    def __init__(this, grid: list[list]):
        this.grid = grid
        this._max_row = len(grid) - 1
        this._max_col = len(grid[0]) - 1
    
    def getLetter(this, pos: Pos) -> str:
        # Check bounds, return `None` if position is invalid.
        if (0 <= pos.row <= this._max_row) and (0 <= pos.col <= this._max_col):
            return this.grid[pos.row][pos.col]
        else:
            return ''


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


# Given the position of the starting letter in a potential word, these functions
#  will check in each valid direction for the remaining letters of the word.
# The functions return the number of words found from the starting point.
def check_horizontals(WS: list[list], start: Pos, target_word: str) -> int:
    words_found = 0
    
    # Horizontal - Right (→)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row, start.col + i)) != target_word[i]: break
    else: words_found += 1
    
    # Horizontal - Left (←)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row, start.col - i)) != target_word[i]: break
    else: words_found += 1
    
    return words_found

def check_verticals(WS: list[list], start: tuple[int, int], target_word: str) -> int:
    words_found = 0
    
    # Vertical - Down (↓)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row + i, start.col)) != target_word[i]: break
    else: words_found += 1
    
    # Vertical - Up (↑)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row - i, start.col)) != target_word[i]: break
    else: words_found += 1
    
    return words_found

def check_diagonals(WS: list[list], start: tuple[int, int], target_word: str) -> int:
    words_found = 0
    
    # Diagonal - Toward NE (↗)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row - i, start.col + i)) != target_word[i]: break
    else: words_found += 1
    
    # Diagonal - Toward SE (↘)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row + i, start.col + i)) != target_word[i]: break
    else: words_found += 1
    
    # Diagonal - Toward NW (↖)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row - i, start.col - i)) != target_word[i]: break
    else: words_found += 1
    
    # Diagonal - Toward SW (↙)
    for i in range(1, len(target_word)):
        if WS.getLetter(Pos(start.row + i, start.col - i)) != target_word[i]: break
    else: words_found += 1
    
    return words_found

def check_cross(WS: list[list], start: tuple[int, int]) -> int:
    return (    # NE (↗) + SW (↙)
        WS.getLetter(Pos(start.row - 1, start.col + 1)) == 'M' and WS.getLetter(Pos(start.row + 1, start.col - 1)) == 'S' or
        WS.getLetter(Pos(start.row - 1, start.col + 1)) == 'S' and WS.getLetter(Pos(start.row + 1, start.col - 1)) == 'M'
    ) and (     # NW (↖) + SE (↘)
        WS.getLetter(Pos(start.row - 1, start.col - 1)) == 'M' and WS.getLetter(Pos(start.row + 1, start.col + 1)) == 'S' or
        WS.getLetter(Pos(start.row - 1, start.col - 1)) == 'S' and WS.getLetter(Pos(start.row + 1, start.col + 1)) == 'M'
    )


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(WS: WordSearch, target_word: str) -> int:
    # Scan through grid, stopping at any 'X's. Check all directions around the 'X' for complete words.
    total_words_found = 0
    for row_index, row in enumerate(WS.grid):
        for col_index, letter in enumerate(row):
            if letter == target_word[0]:
                total_words_found += check_horizontals(WS, Pos(row_index, col_index), target_word)
                total_words_found += check_verticals(WS, Pos(row_index, col_index), target_word)
                total_words_found += check_diagonals(WS, Pos(row_index, col_index), target_word)
    return total_words_found


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(WS: WordSearch) -> int:
    # Scan through grid, stopping at any 'A's. Check diagonals around the 'A' for 'M' and 'S' on opposite sides.
    total_crosses_found = 0
    for row_index, row in enumerate(WS.grid):
        for col_index, letter in enumerate(row):
            if letter == 'A' and check_cross(WS, Pos(row_index, col_index)):
                total_crosses_found += 1
    return total_crosses_found


if __name__ == "__main__":
    input = Setup('day04_input.txt')
    
    target_word = 'XMAS'
    
    grid = []
    for input_line in input:
        if input_line.strip() != '':
            row = list(input_line)
            grid.append(row)
    
    WS = WordSearch(grid)
    
    print(f"[Part 1] 'XMAS' found {Part1(WS, target_word)} times.")
    
    print(f"[Part 2] 'X-MAS' found {Part2(WS)} times.")