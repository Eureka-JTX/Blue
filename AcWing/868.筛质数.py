N=100010
#普通筛
##def sieve():
##    global cnt
##    for i in range(2,n+1):
##        if not st[i]:
##            cnt+=1
# 不管是合数还是质数，都用来筛掉它的倍数
##        for j in range(i,n+1,i):
##            st[j]=True
##    return cnt

#埃氏筛
##def sieve_E():
##    global cnt
##    for i in range(2,n+1):
##        if not st[i]:
##            cnt+=1
# 可以用质数就把所有合数筛掉
##        for j in range(i,n+1,i):
##            st[j]=True
##    return cnt
    
#线性筛
def sieve_L():
    global cnt
    for i in range(2,n+1):
        if not st[i]:
            primes[cnt]=i
            cnt+=1
        for j in range(cnt):
            if primes[j]>n/i:   break
            st[primes[j]*i]=True
            if i%primes[j]==0:  break
    return cnt
    # 内层循环判断primes[j]>n/i就break，保证primes[j]*i < n，st数组不会越界
        
def L():
    global cnt
    for i in range(2,n+1):
        if not st[i]:
            primes[cnt]=i
            cnt+=1
            for j in range(cnt):
                if primes[j]>n/i:   break
                st[primes[j]*i]=True
                if i%primes[j]==0: break
            
primes,cnt,st=[0]*N,0,[False]*N
n=int(input())
print(sieve_L())
