n, k = map(int, input().split())
nums = list(map(int, input().split()))
idx = 0
tmp = 0
cnt = 0

while idx + k <= n:
    if 0 not in nums[idx:idx + k]:
        cnt += 1
        for i in range(idx, idx + k):
            nums[i] -= 1
    else:
        tmp = idx
        idx += nums[idx:idx + k].index(0) + 1
        for i in range(tmp, idx):
            cnt += nums[i]
            nums[i] = 0
for i in range(idx, n):
    cnt += nums[i]
print(cnt)
