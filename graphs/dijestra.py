# {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
# Dijistra Algorithm doesn't work for the negative wieght to why run the below code on this adj  adj=[[1,-2],[0,-2]]
# this algorithm gives the shortest path from source to all other vertices in the graph.
# this algorith is solved using priority queues concept.
# TC-> O(E*log V)
import heapq
def shortestPath(V,adj,S):
    minHeap=[]
    distance=[float("inf")]*V
    distance[S]=0
    heapq.heappush(minHeap,[0,S])
    while minHeap:
        dist,node = heapq.heappop(minHeap)
        for neighbour in adj[node]:
            neighbour_node=neighbour[0]
            neighbour_distance=neighbour[1]
            if(neighbour_distance+distance[node] < distance[neighbour_node]):
                distance[neighbour_node]=neighbour_distance+distance[node]
                minHeap.append([distance[neighbour_node],neighbour_node])
    return distance

print(shortestPath(3,[[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]],2))

