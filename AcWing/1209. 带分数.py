from itertools import permutations as per
def calc(l,r):
    res=0
    for i in range(l,r+1):
        res=10*res+int(p[i])
    return res
        
n=int(input())
cnt=0
for p in per("123456789"):
    a,b,c=0,0,0
    for i in range(7):
        for j in range(i+1,8):
            a,b,c=calc(0,i),calc(i+1,j),calc(j+1,8)
            if a*c+b==n*c:  cnt+=1
print(cnt)

    
