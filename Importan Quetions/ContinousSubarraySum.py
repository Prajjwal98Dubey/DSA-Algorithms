'''
Concept -> it follows the same approach as the subarray sum divisible by k with one improvement.

Consider every index as the last element of the subarray,then try out finding the reminder and if this reminder is seen before then this is sure that there exists a subarray which is divisble my k.

'''
import collections
def checkSubarraySum(nums,k):
    hash = collections.defaultdict(list)
    sum = 0
    hash[0] = [-1]
    for i in range(len(nums)):
        sum+=nums[i]
        if sum%k in hash:
            index = hash[sum%k][0]
            if i - index > 1:
                return True
        hash[sum%k].append(i)
    return False

print(checkSubarraySum([4,2,10,1],6))
    