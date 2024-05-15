'''
Approach:- first find the distances of every cell of the grid from the cell having value of 1 which means we have to apply multisource BFS after this we have to find the range in which the safe factor occurs and then apply binary search to find out the maximum sf.
'''
import collections
def maximumSafenessFactor(grid):
    #Step1:- apply multisource BFS
    ROWS,COLS = len(grid),len(grid[0])
    if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
        return 0
    q = collections.deque()
    visited=set()
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]==1:
                q.append((i,j,0))
                visited.add((i,j))
    mini = float("inf")
    maxi = -float("inf")
    while q:
        row,col,dis = q.popleft()
        mini = min(dis,mini)
        maxi = max(maxi,dis)
        grid[row][col]=dis
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
            r,c = row+nrows,col+ncols
            if r==ROWS or c==COLS or r<0 or c<0 or (r,c) in visited:
                continue
            q.append((r,c,dis+1))
            visited.add((r,c))
    print(grid)
    #Step2 :- find the path with the maximum safest distance.
    def dfs(row,col,sf,visited):
        if row==ROWS-1 and col==COLS-1:
            return True
        if grid[row][col] < sf:
            return False
        visited.add((row,col))
        res = False
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
            r,c = row+nrows,col+ncols
            if r==ROWS or c==COLS or r<0 or c<0 or (r,c) in visited or grid[r][c] < sf:
                continue
            if grid[r][c]>=sf:
                res = res or dfs(r,c,sf,visited)
        return res
    l=mini
    r= maxi
    ans = 0
    while l<=r:
        mid = (l+r)//2
        if dfs(0,0,mid,set()):
            ans = max(ans,mid)
            l=mid+1
        else:
            r=mid-1
    return ans

print(maximumSafenessFactor([[0,1,1],[0,0,0],[0,0,0]]))
    
