import heapq
def minimunDistance(points):
    maxXHeap = []
    maxYHeap = []
    mini=float("inf")
    for i in range(len(points)):
        heapq.heappush(maxXHeap,[-points[i][0],-points[i][1],i])
        heapq.heappush(maxYHeap,[-points[i][1],-points[i][0],i])
    for i in range(len(points)):
        currMax = -1
        xArr = []
        yArr = []
        for point in maxXHeap:
            x,y,index=point
            if index!=i:
                xArr.append(-1*x)
                yArr.append(-1*y)
                break
        for point in maxXHeap[::-1]:
            x,y,index=point
            if index!=i:
                xArr.append(-1*x)
                yArr.append(-1*y)
                break
        currMax=max(currMax,abs(xArr[0]-xArr[1])+abs(yArr[0]-yArr[1]))
        # print(mini)
        xArr1 = []
        yArr1 = []
        for point in maxYHeap:
            y,x,index=point
            if index!=i:
                xArr1.append(-1*x)
                yArr1.append(-1*y)
                break
        for point in maxYHeap[::-1]:
            y,x,index=point
            if index!=i:
                xArr1.append(-1*x)
                yArr1.append(-1*y)
                break
        currMax=max(currMax,abs(xArr1[0]-xArr1[1])+abs(yArr1[0]-yArr1[1]))
        mini = min(mini,currMax)
    return mini


print(minimunDistance([[1,1],[1,1],[1,1]]))
        

            




