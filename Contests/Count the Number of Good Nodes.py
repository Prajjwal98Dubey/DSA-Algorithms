#LC 3249
import collections
def countGoodNodes(edges):
    adj = collections.defaultdict(list)
    hash = {}
    for u,v in edges:
        adj[min(u,v)].append(max(u,v))
        adj[max(u,v)]=[]
        if u not in hash:
            hash[u]=0
        if v not in hash:
            hash[v]=0
    def dfs(node):
        if len(adj[node]) == 0:
            return
        for nei in adj[node]:
            dfs(nei)
            hash[node]+=1+hash[nei]
        return
    dfs(0)
    cnt=0
    print(hash)
    print(adj)
    for key in hash:
        if hash[key]==0:
            cnt+=1
            continue
        flag = 1
        for i in range(len(adj[key])-1):
            if hash[adj[key][i]]!=hash[adj[key][i+1]]:
                flag= 0
                break
        if flag:
            cnt+=1
    return cnt


# testcases = [[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],[[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]],[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]],[[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]]
testcases =[[[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]]

for test in testcases:
    print(countGoodNodes(test))
        