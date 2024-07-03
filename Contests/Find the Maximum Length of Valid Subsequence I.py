
'''
'''
def maximumLength(nums):
    arr = [nums[i]%2 for i in range(len(nums))]
    # dp =[[[[]]]]
    dp=[[[-1 for k in range(4)]for j in range(3)] for i in range(len(nums)+1)]
    def dfs(index,prev,rem):
        if index >= len(arr):
            return 0
        if dp[index][prev+1][rem+1]!=-1:
            return dp[index][prev+1][rem+1]
        nottake =  dfs(index+1,prev,rem)
        take =  0
        if prev==-1 and rem==-1:
            take =  1 + dfs(index+1,arr[index],rem)
        if prev!=-1 and rem==-1:
            take =  1 + dfs(index+1,arr[index],arr[index] + prev)
        if prev!=-1 and rem!=-1:
            if arr[index] + prev == rem:
                take = 1+dfs(index+1,arr[index],rem)
            else:
                take = dfs(index+len(nums)+1,arr[index],rem)
        dp[index][prev+1][rem+1] = max(take,nottake)
        return max(take,nottake)
    return dfs(0,-1,-1)


# print(maximumLength([]))
print(maximumLength([3,7,6]))
print(maximumLength([1,2,3,4]))

