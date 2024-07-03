''' 
amount -> 10^6  

coins => {1,2,3}


'''
def minimizingCoins(nums,target):
    dp=[[0 for j in range(target+1)]for i in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = 0
    for j in range(1,target+1):
        dp[0][j] = j // nums[0] if j % nums[0] ==0 else float("inf")
    for i in range(1,len(nums)):
        for j in range(1,target+1):
            nottake = dp[i-1][j]
            take = float("inf")
            if j - nums[i] >=0:
                take = 1 + dp[i][j-nums[i]]
            dp[i][j] = min(take,nottake)
    # print(dp)
    return dp[len(nums)-1][target] if dp[len(nums)-1][target]!=float("inf") else -1 
print(minimizingCoins([1,5,7],11))