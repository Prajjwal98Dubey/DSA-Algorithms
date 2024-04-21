# Not Correct as of now.
import heapq,collections
def minimumOperations(grid):
    ROWS,COLS = len(grid),len(grid[0])
    curr = -1
    ops = 0
    for c in range(COLS):
        maxHeap = []
        hash =  collections.defaultdict(int)
        for r in range(ROWS):
            hash[grid[r][c]]+=1
        for key in hash:
            heapq.heappush(maxHeap,[-hash[key],-1*key])
        flag = 1
        while maxHeap:
            f,v = heapq.heappop(maxHeap)
            v=-v
            if v!=curr:
                curr = v
                ops+=ROWS-(-1*f)
                flag = 0
                break
        if flag:
            ops+=ROWS
        print("This is the Current Element",curr)
        print("Number of operation in each steps:",ops)
    return ops
        
print(minimumOperations([[4,5,0,1],[1,9,0,8],[2,2,5,3],[2,0,9,3]]))

# 2 3 2 2 