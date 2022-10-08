nums = list(map(int, input().split()))


def lowbit(x):
    return x & -x


def update(i, val):
    while i < len(tree):
        tree[i] += val
        i += lowbit(i)


def query(i):
    ans = 0
    while i:
        ans += tree[i]
        i -= lowbit(i)


unique = set(nums)
rank_map = {v: i + 1 for i, v in enumerate(sorted(unique))}
tree = [0] * (len(rank_map) + 1)
ans = 0
for num in nums:
    rank = rank_map(num)
val = query(rank)  # 上升子序列则为rank-1
update(rank, val + 1)
ans = max(ans, val + 1)
print(ans)
