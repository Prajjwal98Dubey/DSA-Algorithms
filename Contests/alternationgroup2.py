'''
[0,1,0,0,1,0,1][0,1,0,0,1,0,1]
'''
def numberOfAlternatingGroups(colors,k):
    newColors=[]
    for _ in range(2):
        for n in colors:
            newColors.append(n)
    # print(newColors)
    limit = len(colors)-1 + k - 1  # 5 + 5
    r = 0
    tmp = k
    cnt = 0
    while r <= limit:    # [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
        if tmp-1 != 0:
            if newColors[r]!=newColors[r+1]:
                tmp-=1
                r+=1
            else:
                r+=1
                tmp = k
                continue 
        else:
            if newColors[r-1] != newColors[r]:
                # print(r)
                cnt+=1
                r+=1
            else:
                tmp = k
    return cnt
print(numberOfAlternatingGroups([1,1,0,1],4))

            

            

        



        

        
         
         