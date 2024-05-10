# Approach:- consider all the zeros as -1 and then check if the sum has occured before because if it has occured before then the elements between them will form the sum of zero which means equal number of zero and one as we are considering every zero as -1.
import collections
def findMaxLength(nums):
    hash = collections.defaultdict(int)
    sum=0
    maxi=-1
    for i in range(len(nums)):
        n = nums[i]
        if n==0:
            n=-1
        sum+=n
        if sum in hash:
            maxi=max(maxi,i-hash[sum])
        elif sum==0:
            maxi=max(maxi,i+1)
        else:
            hash[sum] = i
    return maxi
print(findMaxLength([0,1,1]))
