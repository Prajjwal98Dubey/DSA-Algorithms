def solve(nums):
  nums.sort()
  cnt = 1
  for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
      cnt+=1
  return cnt
n = int(input())
arr = list(map(int,input().split()))

ans = solve(arr)
print(ans)