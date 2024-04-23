'''
Use of dijstra two times one from the 0th node and other from the (n-1)th node,think like this if we have to check for the particular edge is included in the atleast one shortest paths for example if we want to know the a->b with w weight edge is included or not then we have to take the distance(shortest) from the 0 to a and distance(shortest) from n-1 to b + w should be equal to the shortest path and vice versa(as the edges are bi-direction.)
'''
import collections,heapq
def findAnswer(n,edges):
    ans = [False] * len(edges)
    adj = collections.defaultdict(list)
    for i in range(len(edges)):
        edge  = edges[i]
        u = edge[0]
        v = edge[1]
        w = edge[2]
        adj[u].append([v,w,i])
        adj[v].append([u,w,i])
    def dijistra(src):
        distance = [float("inf")]*n
        minHeap = []
        distance[src] = 0
        heapq.heappush(minHeap,[0,src])
        while minHeap:
            dist,node = heapq.heappop(minHeap)
            if dist > distance[node]:
                continue
            for nei in adj[node]:
                neiNode = nei[0]
                neiDist = nei[1]
                if distance[neiNode] > dist + neiDist:
                    distance[neiNode] = dist + neiDist
                    heapq.heappush(minHeap,[distance[neiNode],neiNode])
        return distance
    startDistance = dijistra(0)
    endDistance = dijistra(n-1)
    # print(startDistance)
    # print(endDistance)
    for i in range(len(edges)):
        edge = edges[i]
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if (startDistance[u] + w + endDistance[v] == startDistance[-1] or startDistance[v] + w + endDistance[u] == startDistance[-1]) and startDistance[-1]!=float("inf"):
            ans[i]=True
    return ans
print(findAnswer(6,[[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]))
                
            


