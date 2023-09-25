# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

list_start = [3, 2, 3, 1, 2, 6, 7, 8, 5, 5, 23, 55, 1]
print(list_start)
new_list = []
for i, num in enumerate(list_start, 1):
    if list_start.count(num) > 1:
        new_list.append(num)
        list_start.remove(num)

print(new_list)
