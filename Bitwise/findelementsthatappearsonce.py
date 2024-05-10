
# not the correct solution.
def search(nums):
    s=""
    maxi=max(nums)
    x = len(format(maxi,'b'))
    for i in range(0,x+1):
        cnt=0
        for n in nums:
            tmp = 1<<i
            if tmp & n:
                cnt+=1
        if cnt==0:
            s+="0"
            continue
        if len(nums) - cnt==0:
            s+="1"
            continue
        if cnt%3==0:
            s+="0"
            continue
        if (len(nums) -cnt) % 3==0:
            s+="1"
            continue
    print(s)
    return int(s,2)

print(search([12, 1, 12, 3, 12, 1, 1, 2, 3, 3]))


