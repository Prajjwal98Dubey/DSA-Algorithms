'''
4 3 5
60 45 80 60    -> 45,60,60,80
30 60 75         -> 30,60,75

desired => 10      actual => 15    k=6


4 <= actual <= 16
'''
def solve(applicants,size,k):
    applicants.sort()
    size.sort()
    cnt = 0
    i=0
    j=0
    cnt=0
    while i<len(applicants) and j < len(size):
        if abs(applicants[i]-size[j]) <=k:
            i+=1
            j+=1
            cnt+=1
        elif applicants[i] > size[j]:
            j+=1
        else:
            i+=1
    return cnt
n,m,k = map(int,input().split())
tmp1 = list(map(int,input().split()))  # applicants
tmp2 = list(map(int,input().split()))  # size of apartments
res = solve(tmp1,tmp2,k)
print(res)