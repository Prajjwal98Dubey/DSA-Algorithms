class DSU:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.size=[1]*(V)
        self.last = V-1
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def rankBySize(self,u,v):
        u_vertex=self.findParent(u)
        v_vertex=self.findParent(v)
        if u_vertex == v_vertex:
            return
        if(self.size[u_vertex] > self.size[v_vertex]):
            self.parent[v_vertex]=u_vertex
            self.size[u_vertex]+=self.size[v_vertex]
        else:
            self.parent[u_vertex]=v_vertex
            self.size[v_vertex]+=self.size[u_vertex]
    def findShortestDistance(self,node,d):
        if node == self.last:
            return 0
        self.findShortestDistance(self.findParent())



def main(n,queries):
    dsu = DSU(n)
    for i in range(n-1):
        if dsu.findParent(i) != dsu.findParent(i+1):
            dsu.rankBySize(i,i+1)
    return dsu.size
print(main(5,[[2,4],[0,2],[0,4]]))

        
