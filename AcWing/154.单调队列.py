##自己写的思路，效率低
##n,k=map(int,input().split())
##a=list(map(int,input().split()))
##N=1000010
##q,h,t,i=[0]*N,0,-1,0
##mam,mim=[],[]
##
##for _ in range(k):
##    t+=1
##    q[t]=a[i]
##    i+=1
##mim.append(min(q[h:t+1]))
##mam.append(max(q[h:t+1]))
##    
##while i<len(a):
##    h+=1
##    t+=1
##    q[t]=a[i]
##    i+=1
##    mim.append(min(q[h:t+1]))
##    mam.append(max(q[h:t+1]))
##
##print(" ".join(map(str,mim)))
##print(" ".join(map(str,mam)))

##官方思路：             该数组为[1 3 -1 -3 5 3 6 7]，k为3。
#q里面装的是a数组的下标（计算范围k内最小和最大值所用到的），
#hh指的是当前滑动窗口最小值的下标存储在q中的哪个位置，
#tt指的是当前滑动窗口（去除掉左边比右边大的数后，严格单调上升）的尾端
#即当前滑动窗口转换成严格单调上升后最大数的下标）在q的哪个位置。
#这道题的核心思想是当前维护的这个范围内是递增的，有个问题是，我们只看见hh在超出范围的时候改变进
# 行+1，假如当前序列为6 4 1 2 3，hh还没超出范围，怎么不改变呢。实际上tt在改变，
# 从而改变了hh。  由于维护的是一个队列，所以hh=0,tt=-1
 
N = 1000010
 
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    q, hh, tt = [0] * N, 0, -1
    for i in range(n):
        while hh<=tt and i-k+1>q[hh]: hh+=1
        while hh<=tt and a[q[tt]]>=a[i]: tt-=1
        tt, q[tt] = tt+1, i
        if i-k+1>=0: print(a[q[hh]], end=" ")
        
    print()
    q, hh, tt = [0] * N, 0, -1
    for i in range(n):
        while hh<=tt and i-k+1>q[hh]: hh+=1
        while hh<=tt and a[q[tt]]<=a[i]: tt-=1
        tt, q[tt] = tt+1, i
        if i-k+1>=0: print(a[q[hh]], end=" ")
