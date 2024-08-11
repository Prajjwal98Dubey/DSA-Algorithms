import collections
def main(edges):
    adj = {}
    tmp = set()
    for u,v in edges:
        if u in adj:
            adj[u].append(v)
            adj[v]=[]
        else:
            adj[u]=[]
            adj[u].append(v)
            adj[v]=[]
    hash = {}
    for key in adj:
        hash[key] = 0
    # print(adj)
    # print(hash)
    def dfs(node):
        if node not in adj:
            return
        for nei in adj[node]:
            dfs(nei)
            hash[node]+=1+hash[nei]
        return
    dfs(0)
    cnt=0
    # print(hash)
    print(hash)
    for key in hash:
        if len(adj[key])==0:
            cnt+=1
            continue
        flag =1 
        for i in range(len(adj[key])-1):
            if hash[adj[key][i]]!=hash[adj[key][i+1]]:
                flag = 0
                break
        if flag:
            cnt+=1
    return cnt
print(main([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))
print(main([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
print(main( [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))