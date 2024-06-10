
# [[0,2],[1,3]]
'''
-> This DFS Approach will give TLE at the last testcase

def swimWater(grid):
    ROWS,COLS =  len(grid),len(grid[0])
    visited = set()
    def dfs(row,col,maxi):
        if row==ROWS-1 and col==COLS-1:
            return max(maxi, grid[row][col])
        visited.add((row,col))
        mini = float("inf")
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
            r,c = row+nrows,col+ncols
            if r<0 or c <0 or r==ROWS or c==COLS or (r,c) in visited:
                continue
            mini = min(mini,dfs(r,c,max(maxi,grid[r][c])))
        visited.remove((row,col))
        return mini
    return dfs(0,0,grid[0][0])

'''

# BFS Approach
import heapq
def swimWater(grid):
    ROWS,COLS = len(grid),len(grid[0])
    minHeap = []
    visited = set()
    heapq.heappush(minHeap,[grid[0][0],0,0])
    while minHeap:
        t,row,col = heapq.heappop(minHeap)
        if row==ROWS-1 and col==COLS-1:
            return t
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1]]:
            r,c = nrows+row,ncols+col
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited:
                continue
            visited.add((r,c))
            heapq.heappush(minHeap,[max(t,grid[r][c]),r,c])
print(swimWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))