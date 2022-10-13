n, x = map(int, input().split())
h = [0] + list(map(int, input().split()))  # 每个石头的高度
p = [0] * int(2e5 + 10)  # 并查集
s = [2 * x] + [0] * int(2e5 + 10)  # 每个石头位置能承载的最大跳跃次数


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def check(mid):
    for i in range(n):
        idx = i + mid
        if idx >= n:
            s[n] += s[i]
        else:
            while 1:
                idx = find(idx)
                mini = min(h[idx], s[i])
                s[idx] += mini
                s[i] -= mini
                h[idx] -= mini
                if h[idx] == 0:
                    p[idx] = idx - 1
                if s[i] == 0:
                    break
                idx = find(idx - 1)
                if idx <= i:
                    return False
    return True


for i in range(n + 1):
    p[i] = i
l, r = 1, n
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)
