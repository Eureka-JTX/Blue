##首先，我们将列表中的区间按照左端点升序排序。
##然后我们将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
##如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，
##那么它们不会重合，我们可以直接将这个区间加入数组 merged 的末尾；
##否则，它们重合，我们需要用当前区间的右端点
##更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。

n = int(input())
a, res = [], []
for _ in range(n):
    l, r = map(int, input().split())
    a.append([l, r])

a = sorted(a, key=lambda x: (x[0], x[1]))

for i in range(n):
    if res:
        if res[-1][1] >= a[i][0]:
            res[-1][1] = max(res[-1][1], a[i][1])
        else:
            res.append([a[i][0], a[i][1]])
    else:
        res.append([a[0][0], a[0][1]])

print(len(res))
