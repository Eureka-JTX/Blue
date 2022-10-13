M = 998244353
n = int(input())
x, y = [0] * (n + 10), [0] * (n + 10)


def fpow(x, y):
    res = 1
    while y:
        if y & 1:
            res *= x % M
        x *= x % M
        y >>= 1
    return res


for i in range(n):
    x[i], y[i] = map(int, input().split())
ans = 0
pre = 1
for i in range(1, n + 1):
    pre *= y[n - i] * fpow(y[n - i] - x[n - i], M - 2) % M
    ans += pre
print(ans % M)
