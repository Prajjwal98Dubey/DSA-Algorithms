def getWordsInLongestSubsequence(n,words,groups):
    # n = 4, words = ["a","b","c","d"], groups = [1,0,1,1]
    ans=[]
    maxi=[]
    maxLen=-1
    def backTrack(index):
        nonlocal maxi
        nonlocal ans
        nonlocal maxLen
        if index==len(words):
            if len(ans.copy()) > maxLen:
                maxLen=len(ans.copy())
                maxi=ans.copy()
            return
        backTrack(index+1)
        if not ans or ans[-1]!=groups[index] :
            ans.append(words[index])
            ans.append(groups[index])
            backTrack(index+1)
            ans.pop()
            ans.pop()
        return
    backTrack(0)
    res=[]
    for i in maxi:
        if i==0 or i==1 or i==2:
            continue
        res.append(i)
    return res

print(getWordsInLongestSubsequence(34,["b","xe","i","j","k","aq","f","a","du","l","c","w","n","v","db","qe","p","fh","u","y","m","h","hr","nk","z","q","s","ke","o","ct","va","uo","qx","ly"],[0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1]))