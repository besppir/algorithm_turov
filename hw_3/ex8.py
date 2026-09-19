import numpy as np
import random

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)

    a = (np.mean(x * y) - np.mean(x) * np.mean(y)) / \
        (np.mean(x ** 2) - np.mean(x) ** 2)

    b = np.mean(y) - a * np.mean(x)

    

    return float(a), float(b)


N = int(input())

a = random.gauss(0, 1)
b = random.gauss(0, 1)

x = []
y = []

for i in range(N):
    x.append(random.gauss(0, 1))
    y.append(a * x[i] + b + random.gauss(0, 1))

print(mnk(x, y))