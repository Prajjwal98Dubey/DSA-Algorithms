# s ="banana" t="ban"
def sequenceCount(s,t):
    def dfs(index1,index2):
        if index2==len(t):
            return 1
        if index1==len(s) and index2!=len(t):
            return 0
        same,notsame = 0,0
        if s[index1]==t[index2]:
            same = dfs(index1+1,index2+1) +  dfs(index1+1,index2)
        else:
            notsame = dfs(index1+1,index2)
        return same + notsame
    return dfs(0,0)

print(sequenceCount("geeksforgeeks","ge"))