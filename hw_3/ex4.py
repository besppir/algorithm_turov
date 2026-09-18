ent = input().split()
size = int(ent[0])
symb = ent[1]
def t(a,b):
    if a % 2 == 0:
        centr=(a//2)*b
        for i in range(1, a // 2):
            print(i*b)
        print(centr)
        print(centr)
        for i in range(a // 2 - 1, 0, -1):
            print(i * b)
    elif a % 2 == 1:
        centr=(a//2+1)*b
        for i in range(1, a // 2 + 1):
            print(i*b)
        print(centr)
        for i in range(a // 2, 0, -1):
            print(i * b)
t(size, symb)