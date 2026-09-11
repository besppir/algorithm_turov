s = input().split()
maxv = None
maxs = 0
for i in s:
    if s.count(i) > maxs:
        maxv = i
        maxs = s.count(i)
print(maxv)