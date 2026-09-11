s = input().split()
g = int(s[0])
text = s[1]
ans = ''
for i in range(0, len(text), g):
    group = text[i:i+g]
    ans += group[::-1]

print(ans)