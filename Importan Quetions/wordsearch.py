def wordSearch(board,word):
    ROWS,COLS = len(board),len(board[0])
    def dfs(row,col,index,visited):
        if index==len(word):
            return True
        if row<0 or col<0 or row==ROWS or col==COLS or (row,col) in visited or board[row][col]!=word[index]:
            return False
        visited.add((row,col))
        res = dfs(row+1,col,index+1,visited) or dfs(row-1,col,index+1,visited) or dfs(row,col+1,index+1,visited) or dfs(row,col-1,index+1,visited)
        visited.remove((row,col))
        return res
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j]==word[0]:
                if dfs(i,j,0,set()):
                    return True
    return False

print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"
))