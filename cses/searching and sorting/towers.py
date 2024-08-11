
def solve(nums):
  res = []
  def bs(target,arr):
    l,r = 0,len(arr)-1
    while l<=r:
      mid=  (l+r)//2
      if arr[mid] > target:
        r= mid-1
      else:
        l = mid+1
    return l
  for n in nums:
    if not res:
      res.append(n)
    else:
      index= bs(n,res)
      if index < len(res):
        res[index] = n
      else:
        res.append(n)
  return len(res)


n = int(input())
arr = list(map(int,input().split()))
ans = solve(arr)

print(ans)