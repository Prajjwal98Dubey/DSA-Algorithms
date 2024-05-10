
def findMinArrowShots(points):
    points.sort(key=lambda x:(x[0],x[1]))
    print(points)
    intervals=[float("inf"),float("inf")]
    cnt=0
    for i in range(len(points)):
        if intervals[0] <= points[i][0] <= intervals[1]:
            intervals[0] = min(intervals[0],points[i][0])
            intervals[1] = min(intervals[1],points[i][1])
        else:
            cnt+=1
            intervals[0] = points[i][0]
            intervals[1] = points[i][1]
    return cnt
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))