import collections
def solve(nums,target):
    hash = collections.defaultdict(list)
    for i in range(len(nums)):
        hash[nums[i]].append(i+1)
    nums.sort()
    l=0
    r=len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return [hash[nums[l]][0],hash[nums[r]][-1]]
        elif nums[l]+nums[r] > target:
            r-=1
        else:
            l+=1
    return []
n,x  = map(int,input().split())
arr=list(map(int,input().split()))
ans = solve(arr,x)
if not ans:
    print("IMPOSSIBLE")
else:
    for n in ans:
        print(n,end=" ")
