# Find the Maximum Number of Elements in Subset LC contest 382
import collections
def maximumLength(nums):
    # create the frequency arr
    hash = collections.defaultdict(int)
    for n in nums:
        hash[n]+=1
    # iterate over the nums
    maxi=hash[1] if hash[1]==0 else (hash[1]-1 if hash[1]%2==0 else hash[1])
    for i in range(len(nums)):
        val = nums[i]
        count=0
        while val <= 10**9 and val!=1 and val in hash and hash[val] >=2:
            count+=2
            val=val*val
        if val in hash:
            count+=1
        else:
            count-=1
        maxi=max(maxi,count)
    return maxi
print(maximumLength([1,1,1,1,1,1,1,1,1,1,1]))