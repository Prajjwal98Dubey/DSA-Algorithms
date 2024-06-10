import collections
import heapq
def sample(rewardValues):
    hash = set()
    nums = []
    for i in range(len(rewardValues)):
        if rewardValues[i] not in hash:
            nums.append(rewardValues[i])
        hash.add(rewardValues[i])
    nums.sort()
    dp = [[0 for _ in range(sum(nums)+sum(nums)+1)] for _ in range(len(nums)+1)]
    for j in range(sum(nums) + sum(nums)+1):
        dp[len(nums)][j]=0
    for i in range(len(nums)-1,-1,-1):
        for j in range(sum(nums),-1,-1):
            notpick = dp[i+1][j]
            pick = 0
            if nums[i] > j:
                pick = nums[i] + dp[i+1][j+nums[i]]
            dp[i][j] = max(pick,notpick)
    return dp[0][0]



print(sample([7]))
print(sample([1,1,3,3]))
print(sample([1,2,3,4,6]))

