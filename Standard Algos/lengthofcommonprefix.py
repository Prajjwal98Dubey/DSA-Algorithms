

def longestCommonPrefix(arr1,arr2):
    hash=set()
    for i in range(len(arr1)):
       s = str(arr1[i])
       "1000"
       for j in range(len(s)):
           hash.add(s[0:j+1])
    maxi=0
    for i in range(len(arr2)):
        s = str(arr2[i])
        for j in range(len(s)):
            if s[0:j+1] in hash:
                maxi=max(maxi,len(s[0:j+1]))
    return maxi
           
print(longestCommonPrefix([1,2,3],[4,4,4]))