'''
def solve(s,dict):
  MOD = (10**9) + 7
  hash = set(dict)
  dp= {}
  def dfs(index):
    if index == len(s):
      return 1
    if index in dp:
      return dp[index]
    t= ""
    ways=0
    for i in range(index,len(s)):
      t+=s[i]
      if t in hash:
        ways+=dfs(i+1)
        ways=ways%MOD  
    dp[index] = ways%MOD
    return ways%MOD
  return dfs(0)

'''

# ababc 
'''
ab
abab
c
cb
'''

def solve(s,dict):
  hash = set(dict)
  dp=[-1] * len(s)

  def dfs(index):
    if index < 0:
      return 1
    ways=0
    t = ""
    for i in range(index,len(s)):
      t+=s[i]
      if t in hash:
        ways+=dfs(i-1)
    return ways
  return dfs(len(s)-1)
n = input()
k = int(input())
words = []
for _ in range(k):
    w = input()
    words.append(w)

ans = solve(n,words)
print(ans)