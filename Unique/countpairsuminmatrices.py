
# March 10 2024 GFG POTD
# Binary Search will give TLE so think of anthor approach
# Try thinking of two pointers such that one pointer will start from the top-left and the second pointer will start from the bottom-right.
def countPairs(mat1,mat2,x):
    ROWS,COLS=len(mat1),len(mat1)
    r1,r2 = 0,ROWS-1
    c1,c2 = 0,COLS-1
    cnt=0
    while r1<ROWS and r2>=0:
        if mat1[r1][c1]+mat2[r2][c2]==x:
            cnt+=1
            c1+=1
            c2+=1
        elif mat1[r1][c1]+mat2[r2][c2]<x:
            c1+=1
        else:
            c2-=1
        if c1>COLS:
            c1=0
            r1+=1
        if c2 > COLS:
            c2=0
            r2-=1
    return cnt
        