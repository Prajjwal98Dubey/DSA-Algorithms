#  every submatrix is the combination of start pair of the submatrix and the end pair of the submatrix.

def getAllSubmatrices(matrix):
    ROWS,COLS = len(matrix),len(matrix[0])
    submatrixes = []
    for r1 in range(ROWS):
        for c1 in range(COLS):
            for r2 in range(r1,ROWS):
                for c2 in range(c1,COLS):
                    sub=[]
                    for row in range(r1,r2+1):
                        tmp = []
                        for col in range(c1,c2+1):
                            tmp.append(matrix[row][col])
                        sub.append(tmp)
                    submatrixes.append(sub)
    return submatrixes
print(getAllSubmatrices([[1,2],[3,4]]))
                
