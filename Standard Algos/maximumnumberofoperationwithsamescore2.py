
def maxOperations(nums):
    def dfs(l,r,target,dp):
        if l>=r:
            return 0
        if (l,r) in dp:
            return dp[(l,r)]
        maxi=0
        if nums[l]+nums[l+1] == target:
            maxi=max(maxi,1+dfs(l+2,r,target,dp))
        if nums[l] + nums[r] == target:
            maxi=max(maxi,1+dfs(l+1,r-1,target,dp))
        if nums[r] + nums[r-1] == target:
            maxi=max(maxi,1+dfs(l,r-2,target,dp))
        dp[(l,r)]=maxi
        return maxi
    maxi=0
    maxi=max(maxi,dfs(0,len(nums)-1,nums[0]+nums[1],{}),dfs(0,len(nums)-1,nums[0]+nums[-1],{}),  dfs(0,len(nums)-1,nums[-1]+nums[-2],{}))
    return maxi

print(maxOperations([3,2,6,1,4]))
    

