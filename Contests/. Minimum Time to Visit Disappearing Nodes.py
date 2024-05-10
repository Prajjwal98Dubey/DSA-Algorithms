import collections,heapq
def minimumTime(n,edges,disappear):
    adj=collections.defaultdict(list)
    for edge in edges:
        u,v,l = edge
        adj[u].append([v,l])
    distance=[float("inf")]*n
    minHeap = []
    heapq.heappush(minHeap,[0,0]) #(distance,node)
    distance[0] = 0
    while minHeap:
        dist,node = heapq.heappop(minHeap)
        for nei in adj[node]:
            neiNode = nei[0]
            neiDist = nei[1]
            if dist + neiDist < distance[neiNode]:
                tmp = distance[neiNode]
                distance[neiNode] = dist + neiDist
                if distance[neiNode] < disappear[neiNode]:
                    heapq.heappush(minHeap,[distance[neiNode],neiNode])
                else:
                    distance[neiNode] = tmp
    # for the nodes which are not connected with 0.
    for i in range(len(disappear)):
        if distance[i]==float("inf"):
            distance[i] = -1
    return distance

print(minimumTime(8,[[4,0,5],[3,7,3],[0,2,3],[3,5,3],[7,0,1],[2,0,3],[7,7,10]],[15,8,4,3,9,18,9,13]))