M = 1e9 + 7
from math import sqrt


def fpow(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a % M
        n >>= 1
        a *= a % M
    return res


def get(x):
    return x * (x + 1) % M * (2 * x + 1) % M


n = int(input())
fac = []
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        fac.append(i)
        fac.append(n // i)
m = len(fac)
ans = 0
for i in range(m):
    ans += get(fac[i]) - get(fac[i - 1])
