import collections
def numberOfSubarrays(nums):
    def previousGreaterElement(nums):
        stack = []
        ans = [-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                ans[index] = i
            stack.append(i)
        return ans
    def bs(arr,leftIndex):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > leftIndex:
                r = mid-1
            if arr[mid] < leftIndex:
                l=mid+1
        return l
    def bsRight(arr,target):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r=mid-1
            else:
                l=mid+1
    pge = previousGreaterElement(nums)
    print(pge)
    hash = collections.defaultdict(list)
    for i in range(len(nums)):
        hash[nums[i]].append(i) 
    subs=0
    for i in range(len(nums)):
        leftBound = bs(hash[nums[i]],pge[i])
        rightBound = bsRight(hash[nums[i]],i)
        subs+=(rightBound-leftBound)+1
    return subs
print(numberOfSubarrays([1]))
