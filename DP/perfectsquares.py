import math
def perfectSquares(n):
    nums=[]
    for i in range(1,n+1):
        sq = math.sqrt(i)
        if sq/int(sq)==1:
            nums.append(i)
    dp=[[0 for j in range(n+1)]for i in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0]=0
    for j in range(n+1):
        dp[0][j]=float("inf")
    for i in range(1,len(nums)+1):
        for j in range(1,n+1):
            nottake = dp[i-1][j]
            take = float("inf")
            if j >=nums[i-1]:
                take  = 1+ dp[i][j-nums[i-1]]
            dp[i][j] = min(take,nottake)
    return dp[len(nums)][n]
    # dp={}
    # def dfs(index,target):
    #     if target == 0:
    #         return 0
    #     if index==0:
    #         return float("inf")
    #     if (index,target) in dp:
    #         return dp[(index,target)]
    #     nottake = dfs(index-1,target)
    #     take = float("inf")
    #     if target>=nums[index-1]:
    #         take = 1 + dfs(index,target-nums[index-1])
    #     dp[(index,target)] = min(take,nottake)
    #     return min(take,nottake)
    # return dfs(len(nums),n)
print(perfectSquares(8609))