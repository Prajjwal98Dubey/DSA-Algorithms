'''
Approach:- just check for the each cell presence in the row or col or in the sqaure,if the encountered cell in present in any row,col,square then it is not the valid sudoku.
create a hash table for each row and col and for square as well.
for sqaure -> consider 3 cell of each row and col as 1 cell that means -> r0,r1,r2 comes in R0 and c0,c1,c2 come in C0.
'''
import collections
def validSuduku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    square = collections.defaultdict(set)
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                continue
            if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in square[(i//3,j//3)]:
                return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            square[(i//3,j//3)].add(board[i][j])
    return True

print(validSuduku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
