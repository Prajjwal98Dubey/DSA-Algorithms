
# def sample(arr1,arr2):
#     ans1,ans2 = [] ,[]
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             ans1.append(str(arr2[j]) +  str(arr1[i]))
#             ans2.append(str(arr1[i]) + str(arr2[j]))
#     # print(ans1)
#     # print(ans2)
#     def findLongest(nums):
#         maxi=-1
#         for i in range(len(nums)):
#             # print(nums[i])
#             s = nums[i]
#             i=0
#             j=len(s)-1
#             while i<=j:
#                 if s[0:i+1] == s[j:]:
#                     # print("here")
#                     maxi=max(maxi,len(s[0:i+1]))
#                 j-=1
#                 i+=1
#         return maxi
#     maxi=-1
#     maxi=max(maxi,findLongest(ans1),findLongest(ans2))
#     return maxi if maxi!=-1 else 0



# print(sample([8],[48]))

import heapq,collections
def sample(grid):
    ROWS,COLS= len(grid),len(grid[0])
    maxHeap=[]
    hash=collections.defaultdict(int)
    def dfs(row,col):
        if row<0 or col<0 or row==ROWS or col==COLS:
            return ""
        if row==ROWS-1 or col==COLS-1:
            return str(grid[row][col])
        res = ""
        for nrows,ncols in [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]:
            rows,cols = row+nrows,col+ncols
            res += str(grid[row][col]) + dfs(rows,cols)
            if int(res) > 10:
                hash[int(res)]+=1
                heapq.heappush(maxHeap,[int(res),hash[int(res)]])
        return
    for i in range(ROWS):
        for j in range(COLS):
            dfs(i,j)
    print(hash)
    return 0

print(sample([[9,7,8],[4,6,5],[2,8,6]]))
