n, m = map(int, input().split())
a, b = [0] * n, [0] * n
totalcnt = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
    if a[i] % b[i] == 0:
        totalcnt += a[i] // b[i]
    else:
        totalcnt += a[i] // b[i] + 1
m = min(m, totalcnt)


def check(x):
    cnt = 0
    for i in range(n):
        if a[i] <= x:  # 先忽略攻击力等于mid的升级
            continue
        cnt += (a[i] - x) // b[i] + 1  # 统计升级次数
    return cnt <= m


# 二分查找最后一次升级最多能提升多少
l, r = 1, 1e6 + 10
while l < r:
    mid = (l + r) // 2
    if check(mid):  # 次数大于m不可取，因此要增加最后一次的提升
        r = mid
    else:
        l = mid + 1

# 先加上攻击力大于mid的技能
ci, res = 0, 0
for i in range(n):
    if a[i] > l:
        len = (a[i] - l) // b[i] + 1
        last = a[i] - (len - 1) * b[i]
        if last == l:
            len -= 1
            last += b[i]
        res += (a[i] + last) * len // 2
        m -= len

print(int(res + m * l))
