import collections
def isPossible(paths): 
    ROWS,COLS=len(paths),len(paths[0])
    adj = collections.defaultdict(list)
    for i in range(ROWS):
        for j in range(COLS):
            if paths[i][j]==1:
                adj[i+1].append(j+1)
    print(adj)
    def dfs(node,ori,visitedNode,visitedEdge):
        visitedNode.add(node)
        if node==ori and len(visitedEdge)!=0 and len(visitedNode)==len(adj):
            print("I came here")
            return True
        res = False
        for nei in adj[node]:
            if ((min(node,nei),max(node,nei)) in visitedEdge):
                continue
            else:
                visitedEdge.add((min(node,nei),max(node,nei)))
                res = res or dfs(nei,ori,visitedNode,visitedEdge)
                visitedEdge.remove((min(node,nei),max(node,nei)))
        return res
    for key in adj:
        if (dfs(key,key,set(),set())):
            return True
    return False


print(isPossible([
               [0,1],
               [1,0]
                ]))
                # [0,1,1,1,1],
                # [1,0,0,1,0],
                # [1,0,0,1,0],
                # [1,1,1,0,1],
                # [1,0,0,1,0]

#                    [0, 1, 1, 0],
#                 [1 ,0 ,1 ,1],
#                 [1 ,1 ,0 ,0],
#                 [0 ,1 ,0 ,0]