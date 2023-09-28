# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

balance = 0
history_of_operations = []
count = 0


def replenishment(withdrow):
    global balance
    global history_of_operations
    global count
    if balance >= 5_0000_000:
        balance *= 0.9
    if count % 3 == 0 and count != 0:
        balance *= 1.03
        count = 0
    if withdrow % 50 == 0:
        balance += withdrow
        count += 1
        history_of_operations.append('+'+str(withdrow))
    return balance


def withdrawal(withdrow):
    global balance
    global history_of_operations
    global count
    if withdrow % 50 == 0:
        commision = withdrow * 0.015
        if commision < 30:
            commision = 30
        elif commision > 600:
            commision = 600
        if (commision + withdrow) <= balance:
            balance -= (withdrow + commision)
            count += 1
            history_of_operations.append('-'+str(withdrow))
        return balance


def operations_history():
    global history_of_operations
    global balance
    print(f'На счету {balance}\n {history_of_operations}')


while True:
    action = input("Выберете операцию 1 - пополнение, 2 - снятие, 3 - история операций, 4 - выход: ")
    if action == '1':
        withdrow = int(input("Введите сумму: "))
        replenishment(withdrow)
    if action == '2':
        withdrow = int(input("Введите сумму: "))
        withdrawal(withdrow)
    if action == '3':
        operations_history()
    if action == '4':
        break
    else:
        continue
print(balance)
