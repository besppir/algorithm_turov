with open ("input.txt") as f:
    s = f.read().split()
res = 0
for i in s:
    if i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
        res += 1
print(res)