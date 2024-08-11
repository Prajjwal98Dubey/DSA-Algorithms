# LC 3224

import collections
def minChanges(nums,k):
    hash = collections.defaultdict(int)
    i,j = 0,len(nums)
    maxi = -1
    cnt=0
    while i < j:
        d = abs(nums[j]-nums[i])
        hash[d]+=1
        i+=1
        j-=1
        maxi = max(maxi,hash[d])
    for key in hash:
        cnt+=hash[key]
    return cnt - maxi

print(minChanges())

            
