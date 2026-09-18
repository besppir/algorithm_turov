def gcd(a,b):
    if b == 0:
        return 1, 0 , a
    x, y, d = gcd(b, a % b)
    return y, x - (a // b) * y, d

a, b = map(int, input().split())

x, y, d = gcd(a, b)

print(x, y, d)
