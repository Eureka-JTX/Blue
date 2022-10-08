s,t=map(int,input().split())
n,a=int(input()),[]
for _ in range(n):
    a.append([int(x) for x in input().split()])
a.sort(key=lambda x:x[0])

flag,i,res=False,0,0
while i<n:
    r=-2e9
    while i<n and a[i][0]<=s:
        r,i=max(r,a[i][1]),i+1
    if r<s: break
    
    res,s=res+1,r
    if r>=t:
        flag=True
        break

if not flag:
        res=-1
print(res)
    
##区间按左端点从小到大排序
##从前往后依次枚举每个区间
##在所有能覆盖 start 的区间中，选择右端点最大的区间，
##然后将 start 更新成右端点的最大值
