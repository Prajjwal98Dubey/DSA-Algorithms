def findDistinctNumber(arr):
    arr.sort()
    cnt=1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            cnt+=1
    return cnt

n = int(input())
nums = list(map(int,input().split()))
res = findDistinctNumber(nums)
print(res)
