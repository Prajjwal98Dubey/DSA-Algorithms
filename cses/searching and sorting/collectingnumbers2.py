def solve(nums,operations):
    pass




n,m = map(int,input().split())
arr = list(map(int,input().split()))
ops = []
for _ in range(m):
    ops.append(list(map(int,input().split())))
ans = solve(arr,ops)
print(ans)