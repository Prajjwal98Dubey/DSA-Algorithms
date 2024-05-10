
def constructList(Q,N):
    ans=[0]
    indexes=[]
    for i in range(len(Q)):
        b,n  = Q[i]
        if b==0:
            ans.append(n)
        else:
            indexes.append((i,n))
    for i in indexes:
        index,n =  i
        for j in range(0,index+1):
            if j < len(ans):
                ans[j]=ans[j] ^ n
    ans.sort()
    return ans

print(constructList([[0, 6],[0, 3], [0, 2], [1, 4], [1, 5]],5))