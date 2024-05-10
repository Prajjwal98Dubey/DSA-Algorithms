
def peakElement(nums):
    l,r=0,len(nums)-1
    while l<=r:
        mid = l+((r-l)//2)
        if (mid-1>0 and nums[mid] < nums[mid-1]):
            r=mid-1
        elif (mid+1<len(nums) and nums[mid] < nums[mid+1]):
            l=mid+1
        else:
            return mid
print(peakElement([1,2]))
