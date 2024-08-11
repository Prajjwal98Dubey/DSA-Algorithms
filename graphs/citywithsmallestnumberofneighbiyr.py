import collections,heapq
def findTheCity(n,edges,distanceThreshold):
    adj = collections.defaultdict(list)
    for u,v,w in edges:
        adj[u].append([v,w])
        adj[v].append([u,w])
    allNodesNearestCities = []
    def dijistra(src):
        distance = [float("inf")]*n
        distance[src] = 0
        minHeap = [] 
        heapq.heappush(minHeap,[src,0])
        while minHeap:
            node,dis = heapq.heappop(minHeap)
            for nei in adj[node]:
                neiNode = nei[0]
                neiDis = nei[1]
                if dis+neiDis < distance[neiNode]:
                    distance[neiNode] = dis+neiDis
                    heapq.heappush(minHeap,[neiNode,distance[neiNode]])
        cnt = 0
        for i in range(len(distance)):
            if i!=src and distance[i] <= distanceThreshold:
                cnt+=1
        allNodesNearestCities.append(cnt)
    for i in range(n):
        dijistra(i)
    smallestDistance = float("inf")
    resCity = -1
    for i in range(len(allNodesNearestCities)):
        if smallestDistance >= allNodesNearestCities[i]:
            smallestDistance = allNodesNearestCities[i]
            resCity = i
    return resCity

print(findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
print(findTheCity(5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))
