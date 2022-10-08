#使用全排列函数，对1~9进行全排列，先验证一下是不是在题目所给的矩阵基础上填写的，再验证是否满足三阶幻方的要求
from itertools import permutations
m=[]
s=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(3):
    m.extend(map(int,input().split()))
    
ans=0
for p in permutations(s):
    flag=True
    for i in range(9):
            if m[i]!=0:
                if m[i]!=p[i]:    flag=False
    if flag==True and p[0]+p[1]+p[2]==p[3]+p[4]+p[5]==p[6]+p[7]+p[8]==p[0]+p[3]+p[6]==p[1]+p[4]+p[7]==p[2]+p[5]+p[8]==p[0]+p[4]+p[8]==p[2]+p[4]+p[6]==15:
        ans+=1
        if ans==1:  res=p
if ans==1:
    for i in range(3):
        print(' '.join(str(j) for j in res[3*i:3*i+3]))
else:
    print("Too Many")
    
