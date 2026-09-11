s = input().split()
s = [int(x) for x in s]
i = 1
if s.count(s[0]) == 1:
    print(s[0])
else:   
    while i <= s[0]:
        if s.count(i) == 0:
            print(i)
            break
        else:
            i += 1
