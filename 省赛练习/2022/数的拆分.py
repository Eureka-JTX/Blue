from math import sqrt

not_prime = [0] * 4010
prime = [0] * 4010
cnt = 1


def check(x):
    y = int(sqrt(x))
    if y * y == x:
        return True
    y = round(x ** (1 / 3), 10)
    if y == int(round(y)):
        return True
    return False


for i in range(2, 4001):
    if not not_prime[i]:
        prime[cnt] = i
        cnt += 1
        for j in range(i + i, 4001, i):
            not_prime[j] = 1

t = int(input())
for i in range(t):
    x = int(input())
    if check(x):
        print("yes")
        continue
    flag = True
    for i in range(1, cnt):
        if x % prime[i] == 0:
            now = 0
            while x % prime[i] == 0:
                now += 1
                x //= prime[i]
            if now == 1:
                flag = False
                break
    if flag and check(x):
        print("yes")
        continue
    else:
        print("no")
