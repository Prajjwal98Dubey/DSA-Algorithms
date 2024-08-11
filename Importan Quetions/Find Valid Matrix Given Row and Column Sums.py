
def findMatrix(rowSum,colSum):
    ROWS = len(rowSum)
    COLS = len(colSum)
    grid = [[0 for _ in range(COLS)]for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            tmp = min(rowSum[r],colSum[c])
            rowSum[r]-=tmp
            colSum[c]-=tmp
            grid[r][c]=tmp
    return grid


print(findMatrix([5,7,10],[8,6,8]))
print(findMatrix([3,8],[4,7]))


