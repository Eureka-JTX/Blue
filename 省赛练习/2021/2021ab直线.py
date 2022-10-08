lines=set()
points=[[i,j] for i in range(20) for j in range(21)]
for i in range(len(points)):
    x1,y1=points[i][0],points[i][1]
    for j in range(i,len(points)):
        x2,y2=points[j][0],points[j][1]
        if x1!=x2:
            k=(y2-y1)/(x2-x1)
            b=(y1*x2-y2*x1)/(x2-x1)
            lines.add((k,b))
print(len(lines)+20)
