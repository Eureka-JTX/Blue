##n=int(input())
##a=list(map(int,input().split()))
##N=120
##stk,t=[0]*N,0
##
##for i in range(n):
##    while t and stk[t]>=a[i]:t-=1
##    if t:
##        print(stk[t],end=" ")
##    else:
##        print("-1",end=" ")
##    t+=1
##    stk[t]=a[i]
##
##补充一个标准库写法：
import collections
n=int(input())
a=list(map(int,input().split()))
stk=collections.deque()

for i in range(len(a)):
    while stk and stk[-1]>=a[i]:
        stk.pop()
    if stk:
        print(stk[-1], end=" ")
    else:
        print("-1", end=" ")
    stk.append(a[i])
