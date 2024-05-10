import collections,heapq
def minValue(s,k):
    hash = collections.defaultdict(int)
    for i in s:
        hash[i]+=1
    maxHeap = []
    for key in hash:
        heapq.heappush(maxHeap,[-hash[key],key])
    while maxHeap and k>0:
        freq , n = heapq.heappop(maxHeap)
        freq = -freq
        freq-=1
        if freq > 0:
            heapq.heappush(maxHeap,[-freq,n])
        k-=1
    ans=0
    while maxHeap:
        freq,n = heapq.heappop(maxHeap)
        ans+=freq*freq
    return ans

print(minValue("abc",3))