n = 2021041820210418
s=set()
res=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        s.add(i)
        s.add(n//i)
for i in s:
    for j in s:
        for k in s:
            if i*j*k==n:
                res+=1
print(res)
        
