N=100010
n=int(input())
w=[]
for _ in range(n):
    w.append([int(x) for x in input().split()])
w.sort(key=lambda x:x[1])

res,right=0,-2e9

for s in w:
    if right<s[0]:
        res+=1
        right=s[1]
print(res)
        
            
