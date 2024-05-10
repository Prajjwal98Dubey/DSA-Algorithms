class DisjointSet:
    def __init__(self,V):
        self.parent=[i for i in range(V)]
        self.size = [1]*(V)   
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def sizeOfNodes(self,u,v):
        u_vertex=self.findParent(u)
        v_vertex=self.findParent(v)
        if u_vertex == v_vertex:
            return 0
        if(self.size[u_vertex] > self.size[v_vertex]):
            self.parent[v_vertex]=u_vertex
            self.size[u_vertex]+=self.size[v_vertex]
        else:
            self.parent[u_vertex]=v_vertex
            self.size[v_vertex]+=self.size[u_vertex]
        return 1
#[[1,2],[0],[0]]
def criticalConnections(v,adj):
    def checkConnected():
        flag=1
        for i in range(1,len(parent)):
            if parent[i]!=parent[i-1]:
                flag=0
                break
        return flag
    dsu = DisjointSet(v)
    edges=[]
    hash=set()
    ans=[]
    for i in range(len(adj)):
        for j in adj[i]:
            edge = (min(i,j),max(i,j))
            if edge not in hash:
                hash.add(edge)
                edges.append(edge)
    for edge in edges:
        for newEdge in edges:
            if edge!=newEdge:
                u1,u2 = newEdge
                dsu.sizeOfNodes(u1,u2)
        parent = dsu.parent
        print(parent)
        # print(dsu.findParent(2))
        flag=1
        for i in range(1,len(parent)):
            if parent[i]!=parent[i-1]:
                flag=0
                break
        if not flag:
            ans.append(edge)
        dsu.parent=[i for i in range(v)]
        dsu.size=[1]*(v)   
    return ans


                  
print(criticalConnections(3,[[1,2],[0],[0]]))