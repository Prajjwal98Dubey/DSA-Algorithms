
def closedIsland(grid):
    ROWS,COLS = len(grid),len(grid[0])
    boundary = set()
    def solve(row,col):
        if row < 0 or col<0 or row==ROWS or col==COLS or grid[row][col] == 1 or (row,col) in boundary:
            return
        boundary.add((row,col))
        solve(row+1,col)
        solve(row-1,col)
        solve(row,col+1)
        solve(row,col-1)
        return
    for r in [0,ROWS-1]:
        for c in range(COLS):
            if grid[r][c] == 0 and (r,c) not in boundary:
                solve(r,c)
    for c in [0,COLS-1]:
        for r in range(ROWS):
            if grid[r][c] == 0 and (r,c) not in boundary:
                solve(r,c)
    visited = set()
    def dfs(row,col):
        if grid[row][col] == 1 or (row,col) in visited:
            return
        visited.add((row,col))
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col-1)
        dfs(row,col+1)
    cnt=0
    for i in range(ROWS):
        for j in range(COLS):
            if (i,j) not in boundary and (i,j) not in visited and grid[i][j]==0:
                dfs(i,j)
                cnt+=1
    return cnt



print(closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]))
print(closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))