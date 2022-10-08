n = int(input())
a = [0] + list(map(int, input().split()))
cnt = [0] * (n + 2)  # 差分数组
sum = [0] * (n + 2)  # 前缀和数组
m = int(input())
old = 0
for i in range(1, n + 1):
    sum[i] = sum[i - 1] + a[i]
for i in range(m):
    l, r = map(int, input().split())
    old += sum[r]-sum[l-1]
    cnt[l] += 1
    cnt[r + 1] -= 1
for i in range(1, n + 1):
    cnt[i] += cnt[i - 1]

a = sorted(a[1:n + 1])
cnt = sorted(cnt[1:n + 1])

new = 0
for i in range(n):
    new += a[i] * cnt[i]
print(new - old)
