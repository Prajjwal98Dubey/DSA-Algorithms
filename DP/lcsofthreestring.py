def lcsOfThree(A,B,C):
    def dfs(index1,index2,index3):
        if index1==len(A) or index2==len(B) or index3==len(C):
            return 0
        match,notmatch=0,0
        if A[index1]==B[index2] and B[index2]==C[index3] and C[index3]==A[index1]:
            match = 1 + dfs(index1+1,index2+1,index3+1)
        else:
            notmatch = max(dfs(index1+1,index2,index3),dfs(index1,index2+1,index3),dfs(index1,index2,index3+1),dfs(index1+1,index2+1,index3),dfs(index1+1,index2,index3+1),dfs(index1,index2+1,index3+1))
        return max(match,notmatch)
    return dfs(0,0,0)

print(lcsOfThree("abcd","efgh","ijkl"))