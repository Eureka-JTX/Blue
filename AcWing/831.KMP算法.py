#暴力算法
##n=int(input())
##p=" "+input()    
##m=int(input())
##s=" "+input()
##
##def match(n,p,m,s):
##    for i in range(1,m+1):
##        flag=True
##        for j in range(1,n+1):
##            if(i+j-1)>m:
##                return
##            if(s[i+j-1]!=p[j]):
##                flag=False
##                break
##        if flag==True:
##            print(i-1,end=" ")
##
##match(n,p,m,s)

##KMP优化 找最长公共前后缀->求next数组(“当前最长公共前后缀长度+1”位与主串当前位比较）
n=int(input())
p=" "+input()    
m=int(input())
s=" "+input()
next,j=[0]*100010,0
for i in range(2,n+1):
    if j==0 or p[i]==p[j+1]:  next[i]=j+1
    else:   j=next[j]
j=0
for i in range(1,m+1):
    while j and s[i]!=p[j+1]:j=next[j]
    if s[i]==p[j+1]:    j+=1
    if j==n:
        print(i-n,end=" ")
        j=next[j]
    
##求next数组代码讲解：https://www.bilibili.com/video/BV16X4y137qw?from=search&seid=18344928365661283657&spm_id_from=333.337.0.0
