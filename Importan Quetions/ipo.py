import heapq
def maximisedCapital(k,w,profits,capital):
    maxHeap = []
    minHeap = [(c,p) for c,p in zip(capital,profits)]
    heapq.heapify(minHeap)
    for _ in range(k):
        while minHeap and minHeap[0][0] <= w:
            c,p = heapq.heappop(minHeap)
            heapq.heappush(maxHeap,-1*p)
        if not maxHeap:
            break
        w+=-1*heapq.heappop(maxHeap)
    return w

        

print(maximisedCapital(2,0,[1,2,3],[0,2,2]))