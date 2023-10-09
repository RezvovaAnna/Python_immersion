# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def random_num_in_name(count, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(count):
            f.write(f'{randint(-1000, 1000)} /{uniform(-1000,1000)} \n')
