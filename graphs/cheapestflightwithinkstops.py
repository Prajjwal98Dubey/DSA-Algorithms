import collections,heapq
def findCheapestFlight(n,flights,src,dst,k):
    adj=collections.defaultdict(list)
    for u,v,cost in flights:
        adj[u].append([v,cost])
    distance=[float("inf")]*n
    distance[src] = 0
    minHeap = []
    heapq.heappush(minHeap,[0,0,src])
    while minHeap:
        stops,dis,node = heapq.heappop(minHeap)
        for nei in adj[node]:
            neiNode = nei[0]
            neiDist = nei[1]
            if neiDist + dis < distance[neiNode]:
                if stops <= k:
                    distance[neiNode] = dis + neiDist
                    heapq.heappush(minHeap,[stops+1,distance[neiNode],neiNode])
    return distance[dst] if distance[dst]!=float("inf") else -1
print(findCheapestFlight(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))