import statistics
n = int(input())
s = list(map(int, input().split()))
if len(s) != n:
    print(f"Ошибка: введено {len(s)} чисел, нужно {n}")
else:
    print(int(statistics.median(s)))