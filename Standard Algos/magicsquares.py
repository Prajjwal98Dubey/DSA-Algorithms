# 1 2 3 4 5 6 7 8 9
def numMagicSquaresInside(grid):
    ROWS,COLS = len(grid),len(grid[0])
    cnt=0
    for r in range(ROWS):
        if r+3 <= ROWS:
            for c in range(COLS):
                if c+3 <= COLS:
                    # print([r,c],end="")
                    hash = set()
                    for i in range(1,10):
                        hash.add(i)
                    prev=-1
                    flag = 1
                    for row in range(r,r+3):
                        s=0
                        for col in range(c,c+3):
                            s+=grid[row][col]
                            hash.remove(grid[row][col]) if grid[row][col] in hash else None
                        if prev==-1:
                            prev = s
                        elif prev!=s:
                            flag = 0
                    for col in range(c,c+3):
                        s=0
                        for row in range(r,r+3):
                            s+=grid[row][col]
                            hash.remove(grid[row][col]) if grid[row][col] in hash else None
                        if prev!=s:
                            flag = 0
                    d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
                    d2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
                    if d1!=prev or d2!=prev:
                        flag = 0
                    if flag and len(hash)==0:
                        cnt+=1
    return cnt


print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))  
print(numMagicSquaresInside([[8]]))
print(numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))     
print(numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]]))  
print(numMagicSquaresInside([[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]))              
#             



# testcases = [[[4,3,8,4],[9,5,1,9],[2,7,6,2]]]
# for test in testcases:
#     print(numMagicSquaresInside(test))


                    



