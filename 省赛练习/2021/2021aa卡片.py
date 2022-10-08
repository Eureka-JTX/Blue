cnt=0
for i in range(1,1000001):
    cnt+=str(i).count('1')
    if cnt>=2021:
        print(i)
        break
