def calc():
    val_1 = int(input('Введите число: '))
    action = input('Выберете действие: ')
    val_2 = int(input('Введите число: '))
    if action == '+':
        summ = int(val_1 + val_2)
        print('Результат: ' + str(summ))
    elif action == '*':
        mult = int(val_1 * val_2)
        print('Результат: ' + str(mult))
    elif action == '/':
        try:
            div = int(val_1 / val_2)
            print('Результат: ' + str(div))
        except ZeroDivisionError:
            if val_2 == 0:
                print('На ноль делить нельзя!')
    elif action == '-':
        sub = int(val_1 - val_2)
        print('Результат: ' + str(sub))
    elif action == '^':
        degree = val_1 ** val_2
        print('Результат: ' + str(degree))
    else:
        print('Такой символ мне не знаком:((')

calc()



