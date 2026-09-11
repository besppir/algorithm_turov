with open("input.txt") as f:
    s = f.read().split()
gl = 'аеёиоуыэюя'
sg = 'бвгджзйклмнпрстфхцчшщьъ'
res =[]
for word in s:
    nw = ''
    for j in range(len(word)):
        nw += word[j]
        if word[j] in gl and j > 0 and word[j-1] in sg:
            nw += 'с' + word[j]
    res.append(nw)
print(res)