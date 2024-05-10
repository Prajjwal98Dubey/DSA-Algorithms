# It will give TLE
# def cherryPickUp(grid):
#     ROWS,COLS = len(grid),len(grid[0])
#     robot1=  []
#     robot2= []
#     def dfs(row,col,robot,path):
#         if row<0 or col<0 or row==ROWS or col==COLS:
#             return
#         if row==ROWS-1:
#             path.append((row,col))
#             if robot==1:
#                 robot1.append(path.copy())
#             if robot==2:
#                 robot2.append(path.copy())
#             path.pop()
#             return
#         path.append((row,col))
#         dfs(row+1,col-1,robot,path)
#         dfs(row+1,col,robot,path)
#         dfs(row+1,col+1,robot,path)
#         path.pop()
#         return
#     dfs(0,0,1,[])
#     dfs(0,COLS-1,2,[])
#     maxi=-1
#     p1=[]
#     p2=[]
#     for r1 in robot1:
#         path=set()
#         sum=0
#         for i in r1:
#             r,c= i
#             path.add((i))
#             sum+=grid[r][c]
#         for r2 in robot2:
#             flag=1
#             for i in r2:
#                 if i in path:
#                     flag=0
#                     break
#             if flag:
#                 s=0
#                 for i in r2:
#                     r,c= i
#                     s+=grid[r][c]
#                     sum+=grid[r][c]
#                 maxi=max(maxi,sum)
#                 sum-=s

#     return maxi


def cherryPickUp(grid):
    ROWS,COLS= len(grid),len(grid[0])
    dp={}
    def dfs(row,col1,col2):
        if col1==COLS or col2==COLS or col1<0 or col2<0:
            return 0
        if col1==col2:
            return 0
        if row==ROWS-1:
            return grid[row][col1] + grid[row][col2]
        if (row,col1,col2) in dp:
            return dp[(row,col1,col2)]
        res =  0
        for dc1 in [-1,0,1]:
            for dc2 in [-1,0,1]:
                res = max(res, grid[row][col1]+grid[row][col2]+dfs(row+1,col1+dc1,col2+dc2))
        dp[(row,col1,col2)] = res
        return res
    return dfs(0,0,COLS-1)
    
print(cherryPickUp([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))