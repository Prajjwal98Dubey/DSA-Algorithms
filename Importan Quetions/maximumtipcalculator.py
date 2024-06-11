# GFG Problem
'''
def maxTip(n,x,y,arr,brr):
    def dfs(index,a,b):
        if a+b == n:
            return 0
        if index == len(arr):
            if a+b==n:
                return 0
            return -float("inf")
        if a+b > n:
            return -float("inf")
        A,B = 0,0
        if a < x:
            A = arr[index] + dfs(index+1,a+1,b)
        if b < y:
            B = brr[index] + dfs(index+1,a,b+1)
        return max(A,B)
    return dfs(0,0,0)
'''

'''
Concept -> not intutive at all but to solve build an array consist of the difference between the arr and brr at every index, then sort it according to the difference from maximum to difference and include the index as well in the new array which is building.
now iterate over the new array after sorting and then calculate the maximum total after taking into  the consideration that at which index which array will give maximum.
'''

def maxTip(n,x,y,arr,brr):
    diff = []
    for i in range(len(arr)):
        diff.append([abs(arr[i]-brr[i]),i])
    diff.sort(key=lambda x:x[0],reverse=True)
    total = 0
    for i in range(len(diff)):
        index = diff[i][1]
        if arr[index] > brr[index]:
            if x > 0:
                x-=1
                total+=arr[index]
            else:
                y-=1
                total+=brr[index]
        else:
            if y > 0:
                y-=1
                total+=brr[index]
            else:
                x-=1
                total+=arr[index]
    return total

print(maxTip(7,3,4,[8, 7, 15, 19, 16, 16, 18],[1, 7, 15, 11, 12, 31, 9]))