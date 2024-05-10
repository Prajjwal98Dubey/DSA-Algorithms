# Approach 1 with the help of heap and hashset

# import heapq
# def bagOfTokensScore(tokens,power):
    # tokens.sort()
    # maxHeap = []
    # for i in range(len(tokens)):
    #     heapq.heappush(maxHeap,[-tokens[i],i])
    # visit = set()
    # maxi = 0
    # curr = 0
    # i=0
    # while i < len(tokens):
    #     if i in visit:
    #         i+=1
    #         continue
    #     if tokens[i] <= power:
    #         power-=tokens[i]
    #         curr+=1
    #         maxi=max(maxi,curr)
    #         visit.add(i)
    #         i+=1
    #     elif tokens[i] > power and curr:
    #         val,index = heapq.heappop(maxHeap)
    #         power+=-1*val
    #         curr-=1
    #         visit.add(index)
    #     else:
    #         i+=1
    # return maxi


# Approach 2 Sorting + two pointers:

def bagOfTokensScore(tokens,power):
    tokens.sort()
    l=0
    r=len(tokens)-1
    maxi=0
    curr=0
    while l<=r:
        if tokens[l] <= power:
            power-=tokens[l]
            l+=1
            curr+=1
            maxi=max(maxi,curr)
        elif tokens[l] > power and curr:
            power += tokens[r]
            r-=1
            curr-=1
    return maxi
print(bagOfTokensScore([200,100],150))