import numpy as np

n, m = map(int, input().split())

a = np.zeros((n, m), dtype=int)

num = 1
top = 0
bottom = n - 1
left = 0
right = m - 1

while top <= bottom and left <= right:

    for j in range(left, right + 1):
        a[top, j] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        a[i, right] = num
        num += 1
    right -= 1


    if top <= bottom:
        for j in range(right, left - 1, -1):
            a[bottom, j] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            a[i, left] = num
            num += 1
        left += 1

for i in range(n):
    a[i] *= i

print(a)