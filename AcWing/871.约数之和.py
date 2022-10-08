# acwing 871. 约数之和
from collections import defaultdict
 
M = int(1e9+7)
 
if __name__ == '__main__':
    primes, ans = defaultdict(int), 1
    n = int(input())
 
    for _ in range(n):
        x = int(input())
        for i in range(2,x+1):
            if i > x/i: break
            while x%i==0:
                primes[i] += 1
                x //= i
        if x>1: primes[x] += 1
 
    for p in primes.items():
        a, b, t = p[0], p[1], 1
        while b:
            t = (t*a+1)
            b -= 1
        ans = ans * t % M
 
    print(ans)
