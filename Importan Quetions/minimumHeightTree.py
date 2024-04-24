'''
Intuition -> The height of the tree if we calculate from the leaf node will always be longer and the height of the tree if we calculate from the centers node will be minimum.
will be using BFS to solve this,we have to keep on cutting the edges until there is one or two nodes left in the graph(draw figures to know why?),the indegree will tell which nodes are the leaf nodes in the tree and we will go from the leaf to the center nodes (will be using queue and only adding the queue when the indegree of the current node is 1 which means when we encounter a leaf node.)
'''
import collections
def findMinHeightTrees(n,edges):
    if n==1:
        return [0]
    q = collections.deque()
    indegree = [0]*n
    adj = collections.defaultdict(list)
    for edge in edges:
        u,v = edge
        adj[u].append(v)
        adj[v].append(u)
        indegree[v]+=1
        indegree[u]+=1
    for i in range(len(indegree)):
        if indegree[i] == 1:
            q.append(i)
    while n>2:
        qlen = len(q)
        n-=qlen
        while qlen:
            node = q.popleft()
            qlen-=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)
    ans =[]
    while q:
        ans.append(q.popleft())
    return ans

print(findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
            

