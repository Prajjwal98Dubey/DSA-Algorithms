import collections
def countGoodNodes(edges):
    adj = collections.defaultdict(list)
    p = {}
    def dfs(node,parent):
        cnt = 1
        p[node] = parent
        for nei in adj[node]:
            if nei!=parent:
                cnt+=dfs(nei,node)
        size[node] = cnt
        return cnt
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    size = {}
    dfs(0,-1)
    # print(size)
    n=len(edges)+1
    good = 0
    for i in range(n):
        prev=-1
        flag = 1
        for nei in adj[i]:
            if nei==p[i]:
                continue
            if prev==-1:
                prev = size[nei]
            elif prev!=size[nei]:
                flag=0
                break
        if flag:
            # print(i,end=" ")
            good+=1
    # print()
    return good
print(countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
print(countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))
print(countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))