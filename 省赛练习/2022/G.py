# from itertools import permutations as per
#
# m = 998244353
#
# n = int(input())
# num = [i for i in range(1, n + 1)]
# cnt = [0] * n
# ans = 0
# for p in per(num):
#     p = list(p)
#     for i in range(n):
#         for j in range(i):
#             if p[j] < p[i]:
#                 cnt[i] += 1
#     ans += sum(cnt)
#     cnt = [0] * n
# print(ans % m)

from math import factorial
n = int(input())
print(factorial(n) *(n-1)*n//4 % 998244353)
