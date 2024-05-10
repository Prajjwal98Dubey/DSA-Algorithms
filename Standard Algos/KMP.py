# first build the LPS (longest prefix suffix)
def KMP(s,pattern):
    def LongestPrefixSuffix(pattern): 
        LPS=[0]*len(pattern)
        prev,i=0,1
        while i<len(pattern):
            if pattern[i]==pattern[prev]:
                LPS[i]=prev+1
                prev+=1
                i+=1
            else:
                if prev==0:
                    LPS[i]=0
                    i+=1
                else:
                    prev=LPS[prev-1]
        return LPS
    LPS = LongestPrefixSuffix(pattern)
    # i = 0
    # j = 0
    # ans=0
    # while i<len(s):
    #     if s[i]==pattern[j]:
    #         i+=1
    #         j+=1
    #     else:
    #         if j==0:
    #             i+=1
    #         else:
    #             j=LPS[j-1]
    #     if j==len(pattern):
    #         ans+=1
    #         i+=1
    #         j=0         
    # return ans
print(KMP("das","asd"))
