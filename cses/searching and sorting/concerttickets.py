
def solve(tickets,nums):
    tickets.sort()
    #[5,5,7,8]  target => 8
    def bs(target,arr):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] < target:
                l = mid+1
            elif arr[mid] > target:
                r = mid-1
            else:
                return mid
        return r if 0 <= r < len(arr) and arr[r] <= target else -1      
    ans = []
    for n in nums:
        index = bs(n,tickets)
        if index !=-1:
            ans.append(tickets[index])
            tickets = tickets[:index] + tickets[index+1:]
        else:
            ans.append(-1)
    return ans

n,m = map(int,input().split())
t = list(map(int,input().split()))
price = list(map(int,input().split()))
res = solve(t,price)
for _ in res:
    print(_)