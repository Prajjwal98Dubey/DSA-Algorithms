
# find all the submatrixes

def countSubMatrices(grid,target):
    res=0
    #func to create all the submatrix
    def subMatrix(r1,r2,c1,c2):
        temp=[]
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                temp.append(grid[i][j])
        return temp
    def sumOfSubMatrix(r1,r2,c1,c2):
        sum=0
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                sum+=grid[i][j]
        return sum
    ROWS,COLS=len(grid),len(grid[0])
    def prefixSumSubMatrix():
        nums=[[0 for _ in range(COLS)]for _ in range(ROWS)]
        for i in range(ROWS):
            sum=0
            for j in range(COLS):
                sum+=grid[i][j]
                nums[i][j]=sum
        return nums
    nums = prefixSumSubMatrix()
    def subMatrixSum(r1,r2,c1,c2):
        sum=0
        for r in range(r1,r2+1):
            sum+=nums[r][c2] - (nums[r][c1-1] if c1-1 >= 0 else 0)
        return sum
    for r in range(ROWS):
        for row in range(r,ROWS):
            for c in range(COLS):
                for col in range(c,COLS):
                    if subMatrixSum(r,row,c,col)==target:
                        res+=1
    return res
print(countSubMatrices([[1,-1],[-1,1]],0))