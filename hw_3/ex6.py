import numpy as np

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)

    a = (np.mean(x * y) - np.mean(x) * np.mean(y)) / \
        (np.mean(x ** 2) - np.mean(x) ** 2)

    b = np.mean(y) - a * np.mean(x)

    return a, b