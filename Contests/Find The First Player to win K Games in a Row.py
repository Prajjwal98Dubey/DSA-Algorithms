'''
[4,2,6,3,9,2,4,3] k = 2

i1 = 2   f = 6
i2 = 4   s = 9


{
  4 : 0,
  2 : 0,
  6 : 1,
  3 : 0
}
'''
import collections
def findWinningPlayer(skills,k):
    hash = collections.defaultdict(int)
    i1,i2 = 0,1
    ans = [-1,-1]
    while skills:
        f = skills[i1]
        s = skills[i2]
        if f > s:
            hash[f]+=1
            if hash[f]==k:
                ans[0] = f
                ans[1] = i1
                break
            skills.append(s)
            hash[s]=0
            i2+=1
        else:
            hash[s]+=1
            if hash[s]==k:
                ans[0] = s
                ans[1] = i2
                break
            skills.append(f)
            hash[f]=0
            i1 = i2+1
        tmp  = i1
        i1 = min(i1,i2)
        i2 = max(tmp,i2)
    return ans[1]

print(findWinningPlayer([2,5,4],3))

            