from heapq import*
n,res=int(input()),0
w=[int(x) for x in input().split()]
heapify(w)
while len(w)>1:
    a,b=heappop(w),heappop(w)
    res+=a+b
    heappush(w,a+b)
print(res)
