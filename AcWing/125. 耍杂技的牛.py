n,w=int(input()),[]
for _ in range(n):
    w.append([int(x) for x in input().split()])
w.sort(key=lamda x:x[0]+x[1])

res,sum=-2e9,0
for i in range(n):
    res=max(res,sum-w[i][1])
    sum+=w[i][0]
print(res)
