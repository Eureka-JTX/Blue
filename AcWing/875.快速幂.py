# acwing 875. 快速幂
 
def qmi(a,k,p):
    res = 1
    while k:
        if k&1: res = res*a % p
        a = a*a % p
        k = k>>1
    return res
 
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a,k,p = map(int,input().split())
        print(qmi(a,k,p))
