n1,n2=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
s=input()
a1=[[i,x] for i,x in enumerate(a1,1)]
a2=[[i,x] for i,x in enumerate(a2,1)]
a1.sort()
a2.sort()
x1,x2=0,0
for i in s:
    if i=='0':
        print("A%d"%a1[x1][0])
        x1+=1
    else:
        print("B%d"%a2[x2][0])
        x2+=1
print('E')
        
