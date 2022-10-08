from heapq import *
n,w=int(input()),[]
for _ in range(n):
    w.append([int(x) for x in input().split()])
w.sort(key=lambda x:x[0])
heap=[]
for i in range(n):
    l,r=w[i]
    if not heap or l<=heap[0]:  heappush(heap,r)
    else:   heapreplace(heap,r)
print(len(heap))
