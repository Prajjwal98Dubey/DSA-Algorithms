import collections
def countingrooms(grid):
    ROWS,COLS = len(grid),len(grid[0])
    cnt=0
    visited = set()
    def bfs(row,col):
        q = collections.deque()
        q.append((row,col))
        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
                rows,cols = nrows+r,ncols+c
                if rows<0 or cols<0 or rows==ROWS or cols==COLS or grid[rows][cols]=="#" or (rows,cols) in visited:
                    continue
                q.append((rows,cols))
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "." and (r,c) not in visited:
                cnt+=1
                bfs(r,c)
    return cnt


n,m = map(int,input().split())
grid=[]
for _ in range(n):
    t=""
    s = input()
    for i in range(len(s)):
        t+=s[i]+" "
    t = t[:len(t)-1]
    grid.append(t.split())
# print(grid)
print(countingrooms(grid))

#. # .

'''
def dfs(row,col):
        if row < 0 or col < 0 or row==ROWS or col==COLS or grid[row][col]=="#" or (row,col) in visited:
            return
        visited.add((row,col))
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)
        return
'''


