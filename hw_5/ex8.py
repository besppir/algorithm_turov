list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

print("Уникальные для первого списка:", set1 - set2)
print("Уникальные для второго списка:", set2 - set1)
print("Уникальные для обоих списков:", set1 ^ set2)
print("Общие числа:", set1 & set2)