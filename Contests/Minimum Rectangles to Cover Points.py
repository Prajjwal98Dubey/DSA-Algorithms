#LC 3111
def minimumRectangleToCoverPoints(points,w):
    points.sort()
    # print(points)
    rec=1
    i=1
    mini=points[0][0]
    while i<len(points):
        if points[i][0] - mini <= w:
            i+=1
            continue
        else:
            mini=points[i][0]
            rec+=1
            i+=1
    return rec
print(minimumRectangleToCoverPoints([[2,3],[1,2]],0))