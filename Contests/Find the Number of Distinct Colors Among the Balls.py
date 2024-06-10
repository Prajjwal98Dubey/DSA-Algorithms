'''
---------------Not Correct Solution-------------------------
'''
import collections
def queryResults(limit,queries):
    lq = collections.defaultdict(int)
    ql = collections.defaultdict(int)
    hash = set()
    ans = []
    for l,q in queries:
        if l not in lq and q not in ql:
            lq[l]=q
            ql[q]=l
            hash.add(q)
            ans.append(len(hash))
            continue
        elif l in lq:
            t = lq[l]
            del lq[l]
            del ql[t]
            hash.remove(t)
            if q not in hash:
                hash.add(q)
            lq[l] = q
            ql[q] = l
            ans.append(len(hash))
            continue
        elif q in ql:
            t = ql[q]
            del ql[q]
            del lq[t]
            ql[q] = l
            lq[l] = q
            ans.append(len(hash))
            continue
    return ans
print(queryResults(1,[[0,1],[1,2],[0,3],[0,2]]))