ent = input().split()
size = int(ent[0])
symb = ent[1]

def up(i, end, b):
    if i > end:
        return
    print(i * b)
    up(i + 1, end, b)

def down(i, b):
    if i == 0:
        return
    print(i * b)
    down(i - 1, b)

def t(a, b):
    centr = (a + 1) // 2

    up(1, centr, b)
    down(centr - 1, b)

t(size, symb)