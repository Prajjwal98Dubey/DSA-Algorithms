# Disjoint set is generally used to find out the number of connected components in O(constant) time In disjoint we have to maintain the rank and parents list to reach to the solution.Disjoint set is solved by union by rank or union by size concepts.
def disjointsSet(V,edges):
    rank=[0]*(V+1)
    parent=[i for i in range(V+1)]
    size=[1]*(V+1)
    def findParent(node):
        if node == parent[node]:
            return node
        parent[node] = findParent(parent[node])
        return parent[node]
    def rank(u,v):
        u_vertex=findParent(u)
        v_vertex=findParent(v)
        if u_vertex==v_vertex:
            return
        if(rank[u_vertex]>rank[v_vertex]):
            parent[v_vertex]=u_vertex
        elif(rank[v_vertex]>rank[u_vertex]):
            parent[u_vertex]=v+v_vertex
        else:
            rank[v_vertex]+=1
            parent[u_vertex]=v_vertex
    def size(u,v):
        u_vertex=findParent(u)
        v_vertex=findParent(v)
        if u_vertex == v_vertex:
            return
        if(size[u_vertex] > size[v_vertex]):
            parent[v_vertex]=u_vertex
            size[u_vertex]+=size[v_vertex]
        else:
            parent[u_vertex]=v_vertex
            size[v_vertex]+=size[u_vertex]



