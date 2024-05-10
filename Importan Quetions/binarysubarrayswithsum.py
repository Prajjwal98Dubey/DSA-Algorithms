# this can be solved using the concept of sum of subarray equal to k.
import collections
def binarySubarraySum(nums,goal):
    hash = collections.defaultdict(int)
    prefix= 0
    hash[0] = 1
    cnt=0
    for i in range(len(nums)):
        prefix+=nums[i]
        if prefix - goal in hash:
            cnt+=hash[prefix-goal]
        hash[prefix]+=1
    return cnt
print(binarySubarraySum([0,0,0,0,0],0))

#this question can be done using two pointer approach which will give the SC as O(1) and TC as O(n).