def solve(movies):
    movies.sort(key=lambda x:x[1])
    r=0
    prev = 0
    cnt = 0
    while r< len(movies):
        if prev <= movies[r][0]:
            cnt+=1
            prev = movies[r][1]
            r+=1
        else:
            r+=1
    return cnt
n = int(input())
meetings  = []
for _ in range(n):
    meetings.append(list(map(int,input().split())))
res = solve(meetings)
print(res)