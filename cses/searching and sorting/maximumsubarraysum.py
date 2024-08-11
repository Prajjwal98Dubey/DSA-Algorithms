def solve(nums):
    curr = 0
    maxi = -float("inf")
    for i in range(len(nums)):
        curr+=nums[i]
        maxi = max(curr,maxi)
        if curr < 0:
            curr = 0
    return maxi
n = int(input())
arr = list(map(int,input().split()))
res =  solve(arr)
print(res)