# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


dict_object = {'палатка': 12, 'термос': 2, 'вода': 6, 'спальный мешок': 9,
               'набор продуктов': 5, 'аптечка': 1, 'одежда': 3, 'гитара': 4}
backpack_capacitys = int(input('Введите вместимость рюкзака: '))
var_backpack = dict(sorted(dict_object.items(), key=lambda x: -x[1]))
print(var_backpack)
contents_backpack = []
for i, k in var_backpack.items():
    if k <= backpack_capacitys:
        contents_backpack.append(i)
        backpack_capacitys -= k
print(f'Можно положить в рюкзак - {contents_backpack}')
