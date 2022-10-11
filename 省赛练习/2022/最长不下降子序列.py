n, k = map(int, input().split())
nums = list(map(int, input().split()))
dpl, dpr = [0] * (n + 1), [0] * (n + 1)


# 子节点信息传递到父节点
def pushUp(root):
    tree[root] = max(tree[2 * root], tree[2 * root + 1])


# 更新最大值
def update(L, val, tleft, tright, root):
    if tleft == tright:
        tree[root] = max(tree[root], val)
        return
    mid = (tleft + tright) // 2
    if L <= mid:
        update(L, val, tleft, mid, 2 * root)
    else:
        update(L, val, mid + 1, tright, 2 * root + 1)
    pushUp(root)


# 查询最大值
def query(L, R, tleft, tright, root):
    if R < tleft or L > tright:
        return 0
    if L <= tleft and R >= tright:
        return tree[root]
    mid = (tleft + tright) // 2
    ans = 0
    if L <= mid:
        ans = max(ans, query(L, R, tleft, mid, 2 * root))
    if R > mid:
        ans = max(ans, query(L, R, mid + 1, tright, 2 * root + 1))
    return ans


# 离散化
uniques = set(nums)
rank_map = {v: i + 1 for i, v in enumerate(sorted(uniques))}

m = len(rank_map)
tree = [0] * (4 * len(rank_map))

ans = k

# 维护出从左到右 i 位置的最长不下降子序列
for i in range(n):
    rank = rank_map[nums[i]]
    val = query(1, rank, 1, m, 1)
    update(rank, val + 1, 1, m, 1)
    dpl[i] = val + 1
    ans = max(ans, dpl[i])

tree = [0] * (4 * len(rank_map))
# 同样维护从右到左 i 位置的最长不上升子序列
for i in range(n - 1, -1, -1):
    rank = rank_map[nums[i]]
    val = query(rank, m, 1, m, 1)
    update(rank, val + 1, 1, m, 1)
    dpr[i] = val + 1
    ans = max(ans, dpr[i])

    # 这里维护的同时要随时与 k 个数前的 dpl[be] 取 max
    be = i - k - 1
    if be >= 0:
        tt = rank_map[nums[be]]
        ans = max(ans, dpl[be] + k + query(tt, m, 1, m, 1))
    # 在比 nums[be] 大的区间中找 max 值，这样才能保证没有遗漏，因为中间可能不止空出 k 个数

# 最后考虑一段最长不下降子序列+k个数的情况
for i in range(n - k):
    ans = max(ans, dpl[i] + k)
for i in range(n - 1, k - 1, -1):
    ans = max(ans, dpr[i] + k)

print(ans)
