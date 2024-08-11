import collections
def labyrinth(grid):
    ROWS,COLS = len(grid),len(grid[0])
    q = collections.deque()
    visited = set()
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "A":
                q.append((0,i,j,""))
                break
    mini = float("inf")
    pathName = ""
    while q:
        dis,row,col,s = q.popleft()
        visited.add((row,col))
        if grid[row][col] == "B":
            if mini > dis:
                mini = dis
                pathName = s
                break
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
            rows,cols = row+nrows,col+ncols
            if rows < 0 or cols < 0 or rows==ROWS or cols == COLS or grid[rows][cols] =="#" or (rows,cols) in visited:
                continue
            q.append((dis+1,rows+1,cols,s+"D"))
            q.append((dis+1,rows-1,cols,s+"U"))
            q.append((dis+1,rows,cols+1,s+"R"))
            q.append((dis+1,rows,cols-1,s+"L"))

    if mini == float("inf"):
         return "NO"
    else:
        return ["YES",mini-1,pathName]

n,m = map(int,input().split())
grid=[]
for _ in range(n):
    t=""
    s = input()
    for i in range(len(s)):
        t+=s[i]+" "
    t = t[:len(t)-1]
    grid.append(t.split())

ans = labyrinth(grid)
if type(ans) == str:
    print(ans)
else:
    for a in range(len(ans)):
        print(ans[a])




'''
visited = set()
    paths = []
    def dfs(row,col,s):
        if row<0 or col<0 or row==ROWS or col==COLS or grid[row][col]=='#' or (row,col) in visited:
            return float("inf")
        if grid[row][col] == 'B':
            paths.append(s)
            return 0
        visited.add((row,col))
        mini = float("inf")
        left = 1 + dfs(row,col-1,s+"L")
        right = 1 + dfs(row,col+1,s+"R")
        up = 1 + dfs(row-1,col,s+"U")
        down = 1 + dfs(row+1,col,s+"D")
        visited.remove((row,col))
        return min(mini,left,right,up,down)   
    pathLen = -1
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "A":
                pathLen = dfs(i,j,"")
                break    
    if pathLen == float("inf"):
        return "NO"
    pathName = ""
    for p in paths:
        if len(p)==pathLen:
            pathName = p
    return ["YES",pathLen,pathName]
'''