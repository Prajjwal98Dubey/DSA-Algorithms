def solve(timings):
    combine = []
    for a,d in timings:
        combine.append([a,1])
        combine.append([d,-1])
    combine.sort(key=lambda x:x[0])  # nlogn
    cnt = 0
    maxi = 0
    for _,d in combine:  # n
        cnt+=d
        maxi = max(maxi,cnt)
    return maxi
n= int(input())
customers = []
for _ in range(n):
    customers.append(list(map(int,input().split())))
ans = solve(customers)
print(ans)
