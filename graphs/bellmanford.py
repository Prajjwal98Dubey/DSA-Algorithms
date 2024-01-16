# Bellman Ford is used to find out the shortest path from source to destination.
# Bellman Ford Algorithm- when our graph contains negative weights then it is not possible to apply dijsitra algorithm, then in this case we will go with the bellman ford algorithm.
# Bellman Ford algorithm is applied in the directed graph(can also be applied in the undirected but we need to convert the undirected graph to directed one.)
# Approach:- run a (n-1) times loop for calculating the distance on every edges which is given.
# it can ony detect negative cylces.
#Code:-
# [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
def bellmanFord(V,edges,S):
    distance=[float("inf")]*V
    distance[S]=0
    for i in range(V-1):
        for j in range(len(edges)):
            u=edges[j][0]
            v=edges[j][1]
            wt=edges[j][2]
            if(distance[u]!=float("inf") and distance[u]+wt<distance[v]):
                distance[v]=distance[u]+wt
    contains_negative_cycle=False
    for j in range(len(edges)):
        u = edges[j][0]
        v = edges[j][1]
        wt = edges[j][2]
        if (distance[u] != float("inf") and distance[u] + wt < distance[v]):
            contains_negative_cycle=True
    if(contains_negative_cycle):
        for i in range(len(distance)):
            distance[i]=-1
    return distance

print(bellmanFord(3,[[0,1,5],[1,0,3],[1,2,-1],[2,0,1]],2))