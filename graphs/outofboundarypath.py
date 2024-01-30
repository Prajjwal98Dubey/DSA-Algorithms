
def findPath(m,n,maxMove,startRow,startColumn):
    ROWS,COLS = m,n
    MOD = (10**9)+7
    def dfs(row,col,move,dp):
        if row==ROWS or row<0 or col==COLS or col<0:
            return 1
        if move==0:
            return 0
        if (row,col,move) in dp:
            return dp[(row,col,move)]
        ans=0
        ans+=dfs(row+1,col,move-1,dp) + dfs(row-1,col,move-1,dp) + dfs(row,col+1,move-1,dp) + dfs(row,col-1,move-1,dp)
        dp[(row,col,move)] = ans
        return ans
    res = dfs(startRow,startColumn,maxMove,{})
    return res % MOD

print(findPath(2,2,2,0,0))