import heapq,collections
def minimizeStringValue(s):
    minHeap=[]
    hash=collections.defaultdict(int)
    for c in s:
        if c!='?':
            hash[c]+=1
    for i in range(ord('a'),ord('z')+1):
        if chr(i) in hash:
            heapq.heappush(minHeap,[hash[chr(i)],chr(i)])
        else:
            heapq.heappush(minHeap,[0,chr(i)])
    # print(minHeap)
    res=[]
    for c in s:
        # print(c)
        if c == '?':
            # print("I am here")
            freq,char = heapq.heappop(minHeap)
            res.append(char)
            freq+=1
            heapq.heappush(minHeap,[freq,char])
            continue
    res.sort()
    print(res)
    i=0
    ans=""
    for c in s:
        if c=="?":
            ans+=res[i]
            i+=1
        else:
            ans+=c
    return ans
print(minimizeStringValue("g?xvgroui??xk?zqb?da?jan?cdhtksme"))
