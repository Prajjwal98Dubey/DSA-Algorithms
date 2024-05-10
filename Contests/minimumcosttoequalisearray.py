def minCostToEqualizeArray(nums,cost1,cost2):
    nums.sort()
    totalSum = sum(nums)
    target = nums[-1] * len(nums)
    def dfs(index,s):
        if s==target and index<0:
            return 0
        if s>target:
            return float("inf")
        if index<0:
            return float("inf")
        p1,p2 = float("inf"),float("inf")
        # pick one index (operation 1)
        p1 = cost1 + dfs(index-1,s+nums[index]+1)
        #pick two indices (operation 2)
        if index-2 >=0:
            p2 = cost2 + dfs(index-2,s+nums[index]+nums[index-1])
        return min(p1,p2)
    return dfs(len(nums)-2,totalSum)

print(minCostToEqualizeArray([2,3,3,3,5],2,1))
    