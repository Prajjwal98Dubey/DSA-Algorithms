''' 
amount -> 10^6  
coins => {1,2,3}
'''
# def minimizingCoins(nums,target):
#     dp = {}
#     def dfs(index,x):
#         if x == 0:
#             return 0
#         if x < 0 or index == len(nums):
#             return float("inf")
#         if (index,x) in dp:
#             return dp[(index,x)]
#         nottake = dfs(index+1,x)
#         take = float("inf")
#         if x - nums[index] >= 0:
#             take = 1 + dfs(index,x-nums[index])
#         dp[(index,x)] = min(take,nottake)
#         return min(take,nottake)
#     res =  dfs(0,target)
#     return res if res!=float("inf") else -1


# def minimizingCoins(nums,target):
#     dp = {}
#     def dfs(index,x):
#         if x == 0:
#             return 0
#         if index == 0:
#             return x // nums[index] if x%nums[index]==0 else float("inf")
#         if (index,x) in dp:
#             return dp[(index,x)]
#         nottake = dfs(index-1,x)
#         take = float("inf")
#         if x - nums[index] >= 0:
#             take = 1 + dfs(index,x-nums[index])
#         dp[(index,x)] = min(take,nottake)
#         return min(take,nottake)
#     res =  dfs(len(nums)-1,target)
#     return res if res!=float("inf") else -1

# def minimizingCoins(nums,target):
#     dp=[[0 for j in range(target+1)]for i in range(len(nums))]
#     for i in range(len(nums)):
#         dp[i][0] = 0
#     for j in range(1,target+1):
#         dp[0][j] = j // nums[0] if j % nums[0] ==0 else float("inf")
#     for i in range(1,len(nums)):
#         for j in range(1,target+1):
#             nottake = dp[i-1][j]
#             take = float("inf")
#             if j - nums[i] >=0:
#                 take = 1 + dp[i][j-nums[i]]
#             dp[i][j] = min(take,nottake)
#     # print(dp)
#     return dp[len(nums)-1][target] if dp[len(nums)-1][target]!=float("inf") else -1 


def minimizingCoins(nums,target):
    dp=[float("inf")]*(target+1)
    dp[0] = 0   # dp[x] -> minimum number of coins to construct x
    for i in range(1,target+1):
        for j in range(len(nums)):  # [7,1,5]
            if (i-nums[j] >= 0):
                dp[i] = min(dp[i],dp[i-nums[j]])
        if dp[i] != float("inf"):
            dp[i]+=1
    return dp[target] if dp[target]!=float("inf") else -1
n,y = map(int,input().split())
nums = list(map(int,input().split()))
ans = minimizingCoins(nums,y)
print(ans)