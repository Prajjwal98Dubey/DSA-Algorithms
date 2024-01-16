# code 1
# Topological sort occurs only in DAG, it states that if u and v have a edge b/w them then 'u' must occur before 'v'.

grid={
    '0':[],
    '1':[],
    '2':['3'],
    '3':['1'],
    '4':['1','0'],
    '5':['0','2'],
}

def dfs(i,visited,grid,stack):
    visited.add(i)
    for neighbour in grid[i]:
        if(neighbour not in visited):
            dfs(neighbour,visited,grid,stack)
    stack.append(i)
def topo_sort(grid):
    visited=set()
    stack=[]
    for i in grid:
        if(i not in visited):
            dfs(i,visited,grid,stack)

    while len(stack)!=0:
        print(stack.pop(),end="")


topo_sort({
    '1':['2'],
    '2':['3'],
    '3':['4','5'],
    '4':['2'],
    '5':[]
})

# code 2
# topological sort only occurs for the DAG(directed acyclic graph)
# Definition of" Topological Sort":- in the linear arrangement, if there is an edge b/w u and v then u should come before v.
# T.C-> O(V+E) ,  S.C-> O(V)
def topoSort(V,adj):
    visited=set()
    stack=[]
    def dfs(v):
        visited.add(v)
        for neighbour in adj[v]:
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(v)
    for i in range(V):
        if i not in visited:
            dfs(i)
    ans=[]
    for i in range(len(stack)):
        ans.append(stack.pop())
    return ans

# Topological Sort with the help of BFS , it is also known an Kahn' algorithm:-
import collections
def topoSort(V,adj):
    indegree=[0]*V
    for vertex in range(V):
        for val in adj[vertex]:
            indegree[val]+=1
    q=collections.deque()
    for i in range(len(indegree)):
        if (indegree[i]==0):
            q.append(i)
    # ans=[]
    count=0
    while q:
        node = q.popleft()
        # ans.append(node)
        count+=1
        for neighbour in adj[node]:
            indegree[neighbour]-=1
            if(indegree[neighbour]==0):
                q.append(neighbour)

    if count==V:
        return True
    else:
        return False
print(topoSort(4,{
    0:[1],
    1:[2],
    2:[3],
    3:[0]
}))




