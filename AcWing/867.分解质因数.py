# acwing 867. 分解质因数
 
def divide(x):
    for i in range(2,x):
        if i>x/i:
            break
        if x%i==0:
            s=0
            while x%i==0:
                x//=i
                s+=1
            print(i,s)
    if x>1: print(x,1)
    print()
            
n = int(input())
for _ in range(n):
    divide(int(input()))
