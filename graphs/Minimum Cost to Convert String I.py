# LC 2976
import collections,heapq
def minimumCost(source,target,original,changed,cost):
    adj = collections.defaultdict(list)
    for i in range(len(original)):
        adj[original[i]].append([changed[i],cost[i]])
    charMap = collections.defaultdict(list)
    def dijistra(src):
        distance = [float("inf")]*26
        distance[ord(src)-ord('a')] = 0
        minHeap = []
        heapq.heappush(minHeap,[0,src])
        while minHeap:
            dis,node = heapq.heappop(minHeap)
            for nei in adj[node]:
                neiNode = nei[0]
                neiDis = nei[1]
                if distance[ord(neiNode)-ord('a')] > dis + neiDis:
                    distance[ord(neiNode)-ord('a')] = dis + neiDis
                    heapq.heappush(minHeap,[distance[ord(neiNode)-ord('a')],neiNode])
        charMap[src] = distance
    for i in range(ord('a'),ord('z')+1):
        dijistra(chr(i))
    c = 0
    for i in range(len(source)):
        if source[i] != target[i]:
            res = charMap[source[i]][ord(target[i])-ord('a')]
            if res == float("inf"):
                return -1
            else:
                c+=res
    return c

print(minimumCost("aabbddccbc","abbbaabaca",["a","b","c","b","a","d"],["d","c","b","d","b","b"],[3,8,7,6,7,10]))