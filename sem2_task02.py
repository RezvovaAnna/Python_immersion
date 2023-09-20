# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

first_fraction = input("Введите первую дробь формате a/b: ").split('/')
first_numerator = int(first_fraction[0])
first_denominator = int(first_fraction[1])
second_fraction = input("Введите вторую дробь формате a/b: ").split('/')
second_numerator = int(second_fraction[0])
second_denominator = int(second_fraction[1])
first_fraction = fractions.Fraction(first_numerator, first_denominator)
second_fraction = fractions.Fraction(second_numerator, second_denominator)
print(f'Сумма при помощи fractions равна - {first_fraction + second_fraction}')
print(f'Произведение при помощи fractions - {second_fraction * first_fraction}')
sum_numerator = 0
multiplication_numerator = 0
common_denominator = 0
integer_part_sum = 0
integer_part_mul = 0
GCD = 0
# Вычисление суммы дробей без выделения целой части
if first_denominator != second_denominator:
    common_denominator = first_denominator * second_denominator
    sum_numerator = (first_numerator * second_denominator) + (
            second_numerator * first_denominator)
    print(f'Сумма без выделения целой части {sum_numerator}/{common_denominator}')
else:
    common_denominator = first_denominator
    sum_numerator = first_numerator + second_numerator
    print(f' Сумма без выделения целой {sum_numerator}/{common_denominator}')
# Выделение целой части у полученной дроби
if sum_numerator / common_denominator > 0:
    integer_part_sum = sum_numerator // common_denominator
    sum_numerator = sum_numerator % common_denominator

print(f'Сумма с выделением целой части - {integer_part_sum} и {sum_numerator}/{common_denominator}')

# Вычисление произведения дробей без выделения целой части
if first_denominator != second_denominator:
    common_denominator = (first_denominator * second_denominator)
    multiplication_numerator = first_numerator * second_numerator
    gcd_1 = common_denominator
    gcd_2 = multiplication_numerator
    # Алгоритм Евклида для поиска НОД, чтобы сократить дробь
    while gcd_1 != 0 and gcd_2 != 0:
        if gcd_1 > gcd_2:
            gcd_1 = gcd_1 % gcd_2
        else:
            gcd_2 = gcd_2 % gcd_1
    GCD = gcd_1 + gcd_2
    if GCD > 0:
        common_denominator = common_denominator // GCD
        multiplication_numerator = multiplication_numerator // GCD
    print(f'Произведение без выделения целой части {multiplication_numerator}/{common_denominator}')
# Выделение целой части у полученной
if multiplication_numerator / common_denominator > 0:
    integer_part_mul = multiplication_numerator // common_denominator
    multiplication_numerator = multiplication_numerator % common_denominator
print(f'Произведение с выделением целой части - {integer_part_mul} и {multiplication_numerator}/{common_denominator}')
