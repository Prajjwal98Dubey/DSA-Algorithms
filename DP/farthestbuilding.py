# [14,3,19,3]
# [1,5,1,2,3,4,10000]
import heapq
def furthestBuilding(heights,bricks,ladders):
    maxHeap = []
    index=0
    for i in range(1,len(heights)):
        if heights[i]<= heights[i-1]:
            continue
        else:
            diff= heights[i] - heights[i-1]
            bricks = bricks-diff
            heapq.heappush(maxHeap,-1*diff)
            if bricks < 0:
                h = -1* heapq.heappop(maxHeap)
                ladders-=1
                bricks=bricks+h



print(furthestBuilding([1,5,1,2,3,4,10000],5,1))