import collections,math
def solve(num1,num2):
    prime=set()
    def isPrime():
        for n in range(1000,10000):
            flag=1
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    flag=0
                    break
            if flag:
                prime.add(n)
    isPrime()
    if num1==num2:
        return 0
    q=collections.deque()
    visited = set()
    q.append((0,str(num1)))
    while q:
        ops,s = q.popleft()
        visited.add(s)
        if int(s) == num2:
            return ops
        for i in range(len(s)):
            for j in range(10):
                tmp=s[:i] + str(j) +s[i+1:]
                if len(str(int(tmp)))==4 and tmp not in visited and int(tmp) in prime:
                    q.append((ops+1,tmp))

print(solve(1373,8179))