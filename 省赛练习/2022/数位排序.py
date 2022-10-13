n, m = int(input()), int(input())
res = {i: sum(list(map(int, list(str(i))))) for i in range(1, n + 1)}
res = sorted(res.items(), key=lambda x: x[1])
print(res[m - 1][0])

# x = [i for i in range(1, n + 1)]
# idx = []
# for i in x:
#     val = list(map(int, list(str(i))))
#     idx.append(sum(val))
# res = [i for _, i in sorted(zip(idx, x))]
# print(res[m - 1])
