def farmLand(land):
    ROWS,COLS=len(land),len(land[0])
    ans=[]
    maxRow=[-1]
    maxCol = [-1]
    visited=[[-1 for _ in range(COLS)]for _ in range(ROWS)]
    def dfs(row,col):
        if row<0 or col<0 or row==ROWS or col==COLS or land[row][col]==0 or visited[row][col]!=-1:
            return
        visited[row][col] = 1
        maxRow[0] = max(maxRow[0],row)
        maxCol[0] = max(maxCol[0],col)
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)
        return
    for i in range(ROWS):
        for j in range(COLS):
            if land[i][j]==1 and visited[i][j]==-1:
                maxRow[0]=-1
                maxCol[0]=-1
                dfs(i,j)
                ans.append([i,j,maxRow[0],maxCol[0]])
    return ans

print(farmLand([[1,0,0],[0,1,1],[0,1,1]]))