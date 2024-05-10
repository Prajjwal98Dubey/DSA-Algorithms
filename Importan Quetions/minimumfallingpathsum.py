'''
Don't take sum as another parameter it will cause TLE.
'''
def minimumFallingSum(matrix):
    ROWS,COLS=len(matrix),len(matrix)
    mini = float("inf")
    def dfs(row,col):
        if row == ROWS or col==COLS or col<0:
            return float("inf")
        if row==ROWS-1:
            return matrix[row][col]
        return min(matrix[row][col] + dfs(row+1,col),matrix[row][col] + dfs(row+1,col-1),matrix[row][col]+ dfs(row+1,col+1))
    for c in range(COLS):
        mini = min(mini,dfs(0,c))
    return mini

print(minimumFallingSum([[-19,57],[-40,-5]]))