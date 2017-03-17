'''
Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules.
It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions
(for example Number of possible chess games at the end of the n-th plies.)
For this mission, we will examine the movements and behavior of chess pawns.
Chess is a two-player strategy game played on a checkered game board laid out in eight rows
(called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares.
Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6").
 For this mission we only need to concern ourselves with pawns.
 A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square.
 For white pawns the front squares are squares with greater row than their.
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
 With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
 We have several white pawns on the chess board and only white pawns.
 You should design your code to find how many pawns are safe.
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.
Precondition:
0 < pawns ≤ 8
'''

def safe_pawns(pawns):
    safe = 0
    for p in pawns:
        safe_row = int(p[1]) - 1
        safe_columns1 = ord(p[0]) - 1
        safe_columns2 = ord(p[0]) + 1
        if safe_row > 0 and (safe_columns1 >= 97 and chr(safe_columns1)+str(safe_row) in pawns) or (safe_columns2 <= 104 and chr(safe_columns2)+str(safe_row) in pawns):
            safe += 1
    return safe

'''
Clear:
1.
def safe_pawns(pawns):
    a = [int(s, 36) for s in pawns]
    return len([x for x in a if x-37 in a or x+35 in a])
'''

    # columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # rows = ['1', '2', '3', '4', '5', '6', '7', '8']
    # safeTotal = 0
    # for p in pawns:
    #     pRow = rows.index(p[1])
    #     if pRow == 0:
    #         continue
    #     pSafeRow = pRow - 1
    #     pColumn = columns.index(p[0])
    #     pSafeColumn1 = pSafeColumn2 = -1
    #     if pColumn != 0:
    #         pSafeColumn1 = pColumn - 1
    #     if pColumn != 7:
    #         pSafeColumn2 = pColumn + 1
    #     if (pSafeColumn1 != -1 and columns[pSafeColumn1] + rows[pSafeRow] in pawns) or (pSafeColumn2 != -1 and columns[pSafeColumn2] + rows[pSafeRow] in pawns):
    #         safeTotal += 1
    # return safeTotal

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1