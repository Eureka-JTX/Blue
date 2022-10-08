M=1010
##第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
##接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
f,s,v,w=[0]*M,[0]*M,[0]*M,[0]*M
N,V=map(int,input().split())

#朴素版
##for i in range(1,N+1):
##    v[i],w[i],s[i]=map(int,input().split())
##for i in range(1,N+1):
##    for j in range(V,v[i]-1,-1):
##        k=0
##        while k*v[i]<=j and k<=s[i]:
##            f[j]=max(f[j],f[j-k*v[i]]+k*w[i])
##            k+=1
##print(f[V])

#二进制优化版
for i in range(1,N+1):
    v[i],w[i],s[i]=map(int,input().split())
    num=min(s[i],V//v[i])
    k=1
    while num>0:
        k*=2
        if k>num:   k=num
        num-=k
        for j in range(V,v[i]*k-1,-1):
            f[j]=max(f[j],f[j-v[i]*k]+w[i]*k)
print(f[V])



for i in range(1,n+1):
    for j in range(v,v[i]-1,-1):
        k=0
        while k<=s[i] and k*v[i]<=j:
            f[j]=max(f[j],f[j-k*v[i]]+k*w[i])
            k+=1

for i in range(1,n+1):
    num=min(s[i],n//v[i])
    k=1
    while num>0:
        k<<=1
        if k>num:   k=num
        num-=k
        for j in range(v,v[i]*k-1,-1):
            f[j]
