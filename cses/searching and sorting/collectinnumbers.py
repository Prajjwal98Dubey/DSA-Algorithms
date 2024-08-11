def solve(nums):
    hash = set()
    rounds = 0
    for n in nums:
        if n-1 not in hash:
            rounds+=1
        hash.add(n)
    return rounds
n = int(input())
arr = list(map(int,input().split()))

ans = solve(arr)
print(ans)