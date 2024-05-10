def longestMonotonicSubarray(nums):
    inc = 0
    l=0
    r=1
    while r < len(nums):
        if nums[r] > nums[r-1]:
            r+=1
            continue
        else:
            inc = max(inc,r-l)
            l=r 
            r+=1
    inc = max(inc,r-l)
    dec = 0
    l=0
    r=1
    while r < len(nums):
        if nums[r] < nums[r-1]:
            r+=1
            continue
        else:
            dec = max(dec,r-l)
            l=r
            r+=1
    dec = max(dec,r-l)
    return max(dec,inc)

print(longestMonotonicSubarray([1,4,3,3,2]))


