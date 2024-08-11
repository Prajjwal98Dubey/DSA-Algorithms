def solve(nums):
    nums.sort()
    flag = 1
    if len(nums)%2==0:
        flag = 0
    if flag:
        actual = nums[len(nums)//2]
        cost = 0
        for n in nums:
            cost+=abs(n-actual)
        return cost
    a1,a2 = nums[len(nums)//2],nums[(len(nums)//2)-1]
    mini = float("inf")
    for a in (a1,a2):
        cost=  0
        for n in nums:
            cost+=abs(n-a)
        mini = min(mini,cost)
    return mini
n = int(input())
sticks = list(map(int,input().split()))
ans = solve(sticks)
print(ans)
