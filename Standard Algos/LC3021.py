# leetcode pe dekho.
# this code will give tle for large testcases
# def findPairs(n,m):
#     pairs = 0
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if (i+j)%2!=0:
#                 pairs+=1
#     return pairs
# def findPairs(n,m):
    # freq=[0]*(10**5)
    # for i in range(1,n+1):
    #     freq[i]+=1
    # for i in range(1,m+1):
    #     freq[i]+=1
    # pairs=0
    # for i in range(1,max(n,m)+1):
    #     for j in range(i+1,max(n,m)+1,2):
    #         p1=i
    #         p2 = j
    #         if p1<= n and p2<=m:
    #             pairs+=1
    #         if p2<=n and p1<=m:
    #             pairs+=1
    # return pairs
# def findPairs(n,m):
#     maxi=m
#     def dfs(index):

#         nottake = dfs(index+2)
#         if index+1<len(maxi)

#     dfs(0)
# print(findPairs(4,4))