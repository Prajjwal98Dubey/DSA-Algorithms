import collections
def maxSelectedArray(nums):
    increased = [i+1 for i in nums]
    hash=collections.defaultdict(list)
    for i in range(len(nums)):
        hash[nums[i]].append(i)
    for i in range(len(increased)):
        hash[increased[i]].append(i)
    newDict=dict(sorted(hash.items(),key=lambda x:x[0]))
    maxi=1
    cnt=1
    for key in newDict:
        if key+1 in newDict and len(newDict[key])!=1:
            cnt+=1
        else:
            maxi=max(maxi,cnt)
            cnt=1
    print(newDict)
    return maxi
print(maxSelectedArray([8,10,6,12,9,12,2,3,13,19,11,18,10,16]))
