def maxScore(grid):
    '''
    recursion + memoization will give TLE
    '''
    ROWS,COLS = len(grid),len(grid[0])
    dp=[[-1 for j in range(COLS+1)]for i in range(ROWS+1)]
    def dfs(row,col):
        if dp[row][col]!=-1:
            return dp[row][col]
        ans = -float("inf")
        for r in range(row+1,ROWS):
            ans = max(grid[r][col] - grid[row][col],ans)
            ans = max(ans,grid[r][col] - grid[row][col] + dfs(r,col))
        for c in range(col+1,COLS):
            ans= max(grid[row][c] - grid[row][col],ans)
            ans = max(grid[row][c] - grid[row][col] + dfs(row,c),ans)
        dp[row][col] = ans
        return ans
    maxi = -float("inf")
    for i in range(ROWS):
        for j in range(COLS):
            maxi = max(maxi,dfs(i,j))
    return maxi
print(maxScore([[4,3,2],[3,2,1]]))