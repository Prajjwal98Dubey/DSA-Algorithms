def minimumOperationsToWriteY(grid):
    ROWS,COLS = len(grid),len(grid[0])
    def minOps(y1,y2):
        ops=0
        for i in range(ROWS):
            for j in range(COLS):
                if((i==j and i<=ROWS//2) or (i+j==ROWS-1 and ROWS//2<=j<COLS) or (ROWS//2<=i<ROWS and j==ROWS//2)):
                    if grid[i][j]!=y1:
                        ops+=1
                else:
                    if grid[i][j]!=y2:
                        ops+=1
        return ops
    return min(minOps(0,1),minOps(0,2),minOps(1,0),minOps(1,2),minOps(2,0),minOps(2,1))
print(minimumOperationsToWriteY([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]))