s=input()
d={}
for i in s:
  d[i]=d.get(i,0)+1
l=sorted(d.items(),key=lambda x:(-x[1],x[0]))
print(l[0][0])
print(l[0][1])

