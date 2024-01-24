# make the use of the sliding window.

def countSubArray(nums,k):
    #find the maximum element
    maxi=max(nums)
    # apply S.W.
    c=0
    l=0
    ans=0
    for r in range(len(nums)):
        if nums[r]==maxi:
            c+=1
        if c==k:
            ans+=len(nums)-r
            while c>=k:
                if nums[l]==maxi:
                    c-=1
                if c>=k:
                    ans+=len(nums)-r
                l+=1
    return ans
print(countSubArray([1,4,2,1],3))