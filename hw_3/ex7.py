import numpy as np

def solve(a):
    a = np.array(a, dtype=float)

    n = len(a)
    m = len(a[0])

    for i in range(n):
        k = i
        while k < n and a[k, i] == 0:
            k += 1

        if k == n:
            continue

        a[[i, k]] = a[[k, i]]

        a[i] = a[i] / a[i, i]

        for j in range(i + 1, n):
            a[j] = a[j] - a[j, i] * a[i]

    for i in range(n - 1, -1, -1):
        for j in range(i):
            a[j] = a[j] - a[j, i] * a[i]

    return a[:, -1]


n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(float, input().split())))

print(solve(a))