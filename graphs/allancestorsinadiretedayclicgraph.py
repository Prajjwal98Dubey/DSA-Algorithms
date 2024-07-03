# import collections
# def getAncestors(n,edges):
#     adj = collections.defaultdict(list)
#     for u,v in edges:
#         adj[u].append(v)
#     ancestors = [[] for i in range(n)]
#     def dfs(node,curr):
#         for nei in adj[curr]:
#             ancestors[node].append(nei)
#             dfs(node,nei)
#     for i in range(n):
#         dfs(i,i)
#     return ancestors


# print(getAncestors(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))

import collections
def getAncestors( n,edges):
    direct_child = collections.defaultdict(list)
    ans = [[] for _ in range(n)]
    for x, y in edges:
        direct_child[x].append(y)

    def dfs(x, curr):
        for ch in direct_child[curr]:
            if ans[ch] and ans[ch][-1] == x: continue
            ans[ch].append(x)
            dfs(x, ch) 

    for i in range(n): dfs(i, i)
    return ans

print(getAncestors(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
