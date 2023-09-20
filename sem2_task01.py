# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

input_num = int(input("Введите целое число: "))
number = input_num
HEX_INDEX = 16
result = ' '
hex_result = hex(input_num)
# Перевод числа в шестнадцатеричное строковое представление
while input_num > 0:
    result = str(input_num % HEX_INDEX) + result
    input_num = input_num // HEX_INDEX
    if result.find('10') != -1:
        result = result.replace('10', 'a')
    elif result.find('11') != -1:
        result = result.replace('11', 'b')
    elif result.find('12') != -1:
        result = result.replace('12', 'c')
    elif result.find('13') != -1:
        result = result.replace('13', 'd')
    elif result.find('14') != -1:
        result = result.replace('14', 'e')
    elif result.find('15') != -1:
        result = result.replace('15', 'f')

# Сравнение с результатом функции hex
if result != hex_result[2:]:
    print(f"Что-то пошло не так: {number} - получилось как {result}"
          f"в шестнадцатеричном представлении, а должно быть {hex_result[2:]}")
if result == hex_result[2:]:
    print(
        f"Все получилось: {number} - это {hex_result[2:]} в шестнадцатеричном представлении. "
        f"А у нас как раз получилось {result}")

# Оба результата строковый тип, но они оказываются не равны. ?
print(type(result), type(hex_result))
print(result == hex_result[2:])

