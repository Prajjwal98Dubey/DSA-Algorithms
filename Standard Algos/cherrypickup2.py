def cherryPickup(grid):
    ROWS,COLS=len(grid),len(grid[0])
    count=[0]
    visited=set()
    def dfs(row,col):
        if row<0 or col<0 or row==ROWS or col==COLS:
            return 0
        maxi=-1
        if (row,col) not in visited:
            visited.add((row,col))
            maxi= max(maxi,grid[row][col] + dfs(row+1,col+1),grid[row][col] + dfs(row+1,col-1),grid[row][col] + dfs(row+1,col))
        return maxi
    print(dfs(0,0))
    return dfs(0,COLS-1)
    print(count[0])
    # print(grid)
    # dfs(0,COLS-1)
    # return count[0]

print(cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))