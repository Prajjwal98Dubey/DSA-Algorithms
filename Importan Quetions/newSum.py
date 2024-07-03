def tmpSum(c):
    for i in range(c+1):
        x = c - (i*i)
        if x > 0:
            n = x**(1/2)
            tmp = round(n)
            if (tmp*tmp) == (n*n):
                return True
    print(round(5**(1/2)))
    return False

print(tmpSum(3))