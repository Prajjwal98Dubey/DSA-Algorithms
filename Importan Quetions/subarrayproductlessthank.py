
def numSubarrayProductLessThanK(nums,k):
    ans = 0
    prod = 1
    l=0 
    for r in range(len(nums)):
        prod*=nums[r]
        while l<=r and prod>=k:
            prod = prod // nums[l]
            l+=1
        ans +=(r-l+1)
    return ans