import collections,heapq
def frequentPrime(grid):
    def isPrime(n):
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    ROWS,COLS= len(grid),len(grid[0])
    hash=collections.defaultdict(int)
    def dfs(row,col,rows,cols,s):
        if row<0 or col<0 or col==COLS or row==ROWS:
            return
        res = str(grid[row][col])
        s+=res
        if int(s) > 10:
            # ans.append(s)
            hash[s]+=1
        dfs(row+rows,col+cols,rows,cols,s)
        return
    for i in range(ROWS):
        for j in range(COLS):
            for nrows,ncols in [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]:
                dfs(i,j,nrows,ncols,"")
    if len(hash)==0:
        return -1
    maxHeap=[]
    for key in hash:
        if (isPrime(int(key))):
            heapq.heappush(maxHeap,[-hash[key],-int(key)])
    if not maxHeap:
        return -1
    freq,n = heapq.heappop(maxHeap)
    return -n
#['1','19','191']
print(frequentPrime([[1,1],[9,9],[1,1]]))