'''
Bipartite Graph -> a graph which can be colored with 2 colors such that no two adjacent nodes have the same color.

or it can also be defined as if we split the nodes into two sets then every node in the set A must have a edge with atleast one node in the set B.
'''
import collections
def isGraphBipartite(graph):
    colors = [-1] * len(graph)   # initially no set is formed
    def bfs(node):
        if colors[node]!=-1:
            return True
        q = collections.deque()
        q.append(node)
        colors[node] = True
        while q:
            n = q.popleft()
            for nei in graph[n]:
                if colors[nei]==colors[n]:
                    return False
                if colors[nei]==-1:
                    colors[nei]= not colors[n]
                    q.append(nei)
        return True
    for i in range(len(graph)):   
        if not bfs(i):
            return False
    return True


testcases = [[[1,3],[0,2],[1,3],[0,2]],[[1,2,3],[0,2],[0,1,3],[0,2]]]

for t in testcases:
    print(isGraphBipartite(t))