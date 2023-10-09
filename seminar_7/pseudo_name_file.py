# Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

__all__ = ['rnd_name', 'pseudo_name_for_file', '_VOWELS']
from random import randint
_VOWELS = "AEYUIOaeuioy"


def rnd_name():
    name_len = randint(4, 7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))
            for i in name:
                if i in _VOWELS:
                    return name.capitalize()


def pseudo_name_for_file(count, file_name):
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(rnd_name()+"\n")

if __name__ == '__main__':
    pseudo_name_for_file(5, r"python part 2\sem7\names.txt")
