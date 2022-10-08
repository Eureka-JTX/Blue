def init(a):
    cnt=1
    while(a):
        if a&1:
            num[cnt]+=1
        cnt+=1
        a>>=1
        
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    n=a[0]
    num=[0]*23
    sum=0
    for i in range(1,n+1):
        init(a[i])
        sum^=a[i]
    if not sum:
        print(0)
    else:
        for i in range(20,0,-1):
            if num[i]==1:
                print(1)
                break
            elif num[i]%2==1:
                if n%2==1:
                    print(1)
                else:   print(-1)
                break
    
    
