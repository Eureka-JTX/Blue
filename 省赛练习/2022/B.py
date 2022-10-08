cond = {187: 0, 2: 1, 3: 2, 5: 4, 7: 4, 13: 10, 19: 18, 23: 15, 29: 16, 31: 27, 37: 22, 41: 1, 43: 11, 47: 5}
div = list(cond.keys())
rem = list(cond.values())
length = len(div)

beta = 1
for i in div:
    beta *= i

alpha = 0
for i in range(length):
    least = beta // div[i]
    k = least
    while k % div[i] != 1:
        k += least
    alpha += k * rem[i]
print(alpha % beta)
