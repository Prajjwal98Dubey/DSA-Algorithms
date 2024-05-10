#find number of subarray where the boundary element is maximum.
import collections
def numberOfSubarrays(nums):
    def nextGreaterElement(arr):
        nge = [len(arr)]*len(arr)
        stack =[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                index = stack.pop()
                nge[index] = i
            stack.append(i)
        return nge
    def bs(arr,index):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > index:
                r=mid-1
            if arr[mid] < index:
                l=mid+1
        return r
    def bsLeft(arr,target):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r=mid-1
            else:
                l=mid+1
    nge = nextGreaterElement(nums)
    hash = collections.defaultdict(list)
    for i in range(len(nums)):
        hash[nums[i]].append(i)
    # print(nge)
    subs = 0
    for i in range(len(nums)):
        r = bs(hash[nums[i]],nge[i])
        l = bsLeft(hash[nums[i]],i) 
        subs+=(r-l+1)
    return subs
print(numberOfSubarrays([3,3,3]))