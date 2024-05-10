# Graph-> DFS and BFS 
# representation of a graph -> adjacency matrix and adjacency list. 

#DFS for a graph  -> TC: O(V+E) and SC: O(V)

# def main(V,adj):
#     visited = set()
#     ans=[]
#     def dfs(node):
#         if node in visited:
#             return
#         visited.add(node)
#         ans.append(node)
#         for nei in adj[node]:
#             dfs(nei)
#     dfs(0)
#     return ans

# print(main(5,[[2,3,1] , [0], [0,4], [0], [2]]))

# BFS of a graph  -> TC: O(V+E) and SC: O(V)

# import collections
# def bfs(V,adj):
#     q = collections.deque()
#     ans = []
#     q.append(0)
#     visited = set()
#     while q:
#         node = q.popleft()
#         if node not in visited:
#             ans.append(node)
#             visited.add(node)
#         for nei in adj[node]:
#             if nei not in visited:
#                 q.append(nei)
#     return ans
# print(bfs(2,[1232]))

# Dijestra Algorithm:- It is used to find out the shortest distance from the source to destination.   TC->ElogV and SC:O(V+E)
# It cannot be applied to the negative weights.
import heapq
def dijkstra(V,adj,S):
    distance = [float("inf")]*V
    minHeap = []
    distance[S]=0
    heapq.heappush(minHeap,[0,S])
    while minHeap:
        dis,node = heapq.heappop(minHeap)
        for nei in adj[node]:
            neiNode = nei[0]
            neiDist = nei[1]
            if neiDist + dis < distance[neiNode]:
                distance[neiNode] = neiDist + dis
                heapq.heappush(minHeap,[distance[neiNode],neiNode])
    return distance

#Topological Sort:- if there is an edge b/w u and v and then u should appear before v.and this is only applied in DAG
# this can be implemented in two ways -> DFS(stack) and BFS(indegree)

#BFS
import collections
def topoSort(V,adj):
    indegree=[0]*V
    for node in adj:
        for v in node:
            indegree[v]+=1
    q = collections.deque()
    for i in range(len(indegree)):
        if indegree[i]==0:
            q.append(i)
    ans = []
    while q:
        node = q.popleft()
        ans.append(node)
        for n in adj[node]:
            indegree[n]-=1
            if indegree[n]==0:
                q.append(n)
    return ans
print(topoSort())