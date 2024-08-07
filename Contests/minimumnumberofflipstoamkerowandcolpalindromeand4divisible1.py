'''
m -> ROWS
n -> COLS
for every (i,j) we need to check these four coordinates (i,j),(m-1-i,j),(i,n-1-j),(m-1-i,n-1-j) this will tell flips to make the rows and cols both palindrome.

'''
def minFlips(grid):
    ROWS,COLS = len(grid),len(grid[0])
    flips=0   # min flips to make the rows and cols both palindrome.
    for i in range(ROWS//2):
        for j in range(COLS//2):
            countOnes=0
            countZeros=0
            if grid[i][j]==1:countOnes+=1
            else:countZeros+=1
            if grid[ROWS-1-i][j]==1:countOnes+=1
            else:countZeros+=1
            if grid[i][COLS-1-j]==1:countOnes+=1
            else:countZeros+=1
            if grid[ROWS-1-i][COLS-1-j]==1:countOnes+=1
            else:countZeros+=1
            # countOnes = 3 countZeros = 1
            flips+=min(countZeros,countOnes)
    print(flips)
    # if i do not add any other 1 in this case.
    if(COLS%2):
        low=0
        high = ROWS-1
        one_one_pair = 0
        one_zero_pair=  0
        c = COLS//2
        if ROWS%2==1 and grid[ROWS//2][c]==1:
            flips+=1
            grid[ROWS//2][c]=0
        while high > low:
            if grid[low][c]==grid[high][c] and grid[low][c]==1:
                one_one_pair+=1
            if grid[low][c]!=grid[high][c]:
                one_zero_pair+=1
            low+=1
            high-=1
        if one_one_pair%2==0:
            flips+=one_zero_pair
        else:
            if one_zero_pair >=1:
                flips+=1
                one_zero_pair-=1
                flips+=one_zero_pair
            else:
                flips+=2
                one_one_pair-=1
    print(flips)
    if(ROWS%2):
        low=0
        high = COLS-1
        one_one_pair = 0
        one_zero_pair=  0
        r = ROWS//2
        if COLS%2==1 and grid[r][COLS//2]==1:
            flips+=1
        while high > low:
            if grid[r][low]==grid[r][high] and grid[r][low]==1:
                one_one_pair+=1
            if grid[r][low]!=grid[r][high]:
                one_zero_pair+=1
            low+=1
            high-=1
        if one_one_pair%2==0:
            flips+=one_zero_pair
            print("from one to one")
        else:
            if one_zero_pair >=1:
                flips+=1
                one_zero_pair-=1
                flips+=one_zero_pair
            else:
                print("from here")
                flips+=2
    return flips



# print(minFlips([[1,0,0],[0,1,0],[0,0,1]]))
# print(minFlips([[0,1],[0,1],[0,0]]))
# print(minFlips([[1],[1]]))

# print(minFlips([[1,1]]))
# print(minFlips([[0,0,1,1],[0,0,0,1]]))
print(minFlips([[0,0,1],[0,0,1],[1,0,1],[1,0,0],[0,1,1]]))   # not working

            

            



    

