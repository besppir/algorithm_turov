num = int(input())
res = [1]
while num > 1:
    for i in range(2, num+1):
        if num % i == 0:
            res.append(i)
            num //= i
            break
print(res)