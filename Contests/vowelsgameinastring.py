# LC 3227



'''
"leetcoder"   

cnt -> 4

1 ->3
2 -> 1
1->1


'''
import collections
def doesAliceWin(s):
    flag = 1
    hash = 0
    vowels = set(['a','e','i','o','u'])
    for c in s:
        if c in vowels:
            hash+=1
    if hash == 0 : return False
    while hash >= 0:
        if flag:
            if hash < 0 : return False
        else:
            if hash-2 < 0 : return True
            hash-=2
        flag = not flag
print(doesAliceWin("leetcoder"))  # True
print(doesAliceWin("bbcd"))  # False
print(doesAliceWin("bac"))  # True


    

