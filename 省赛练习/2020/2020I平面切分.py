n=int(input())
line=set()
for i in range(n):
  line.add(tuple(map(int,input().split())))
lines=list(line)
n=len(lines)

p=2
if n==1:
  print(p)
else:
  for i in range(1,n):
    point=set()
    for j in range(i):
      if lines[i][0]!=lines[j][0]:
        x=(lines[i][1]-lines[j][1])/(lines[j][0]-lines[i][0])
        y=lines[i][0]*x+lines[i][1]
        point.add((x,y))
    p+=len(point)+1
  print(p)
