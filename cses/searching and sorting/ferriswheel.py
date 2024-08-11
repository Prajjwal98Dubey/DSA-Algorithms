
def solve(nums,wt):
    nums.sort()
    cnt=0
    curr = 0
    i = 0
    j=len(nums)-1
    while j > i:
        if nums[j] + nums[i] <= wt:
            i+=1
            j-=1
            cnt+=1
        else:
            j-=1
            cnt+=1
    return cnt+1 if i==j else cnt
n,w = map(int,input().split())
tmp1 = list(map(int,input().split()))  
res = solve(tmp1,w)
print(res)