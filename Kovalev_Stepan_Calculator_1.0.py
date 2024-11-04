print('Здраствуйте, пользователь! Это калькулятор, он умеет:') #начало/start
print(' - сложение(1)')
print(' - вычитание(2)')
print(' - умножение(3)')
print(' - деление(4')
print(' - целочисленное деление(5)')
print(' - взятие остатка(6)')
print(' - возведение в степень(7)')
print(' - квадратный корень числа(8)')
print(' - переводить из любой системы счисления в десятичную(9)')
print(' - анализ числа(10)')
print('В анализ числа входит:')
print(' - Вывод количества разрядов в числе(1)')
print(' - Четное или не четное число(2)')
print(' - Вывод суммы цифр числа(3)')
print(' - проверку является ли число простым, если не простое, то вывести все делители числа(4)')
print(' - проверку ли число полным квадратом(5)')
print(' - проверить, является ли число полным кубом(6)')
print('Это всё что может выполнить данный калькулятор')
print('Правила ввода:')
print(' - в поле ввода чисел вводить только числа с помощью цифр, не буквами')
print(' - в поле ввода операции или анализа вводить число указанное справа')
print(' - если нужно ввести буквы, используйте заглавные английские буквы')
print(' - если вы захотите продолжить, в ответ напишите "Да" без ковычек')
print(' - когда хотите посчитать корень, в ответ впишите неотрицательное число')
print(' - Делить на ноль нельзя!')
print(' - перевод в десятичную систему работает только до 36 системы')
print('Теперь приступим к работе.')
answ = True
def addition(x, y): #функции/defs
   return x + y


def substraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def compertition(x, y):
    return x / y


def integer_division(x, y):
    return x // y


def seizure_remainder(x, y):
    return x % y


def involution(x, y):
    return x ** y


def square(x):
    return x ** 0,5


def intergration(x, base):
    number = str(number)
    base = int(base)
    try:
        return int(number, base)
    except ValueError:
        return None


while answ:
    num1 = input('Введите первое число: ')
    oper = int(input('Введите номер операции: '))
    while oper == 7 and int(num1) < 0:
        print('Квадратный корень отрицательного числа вычислить нельзя числа! Либо замените число, либо операцию')
        num1 = input('Введите первое число: ')
        oper = int(input('Введите номер операции: '))
    if oper == 1 or oper == 2 or oper == 3 or oper == 4 or oper == 5 or oper == 6 or oper == 7:
        num2 = float(input('Введите второе число: '))
        while oper == 4 and num2 == 0 or oper == 5 and num2 == 0 or oper == 6 and num2 == 0:
            print('Делить на ноль нельзя! Либо замените число, либо операцию')
            oper = int(input('Введите номер операции: '))
            num2 = float(input('Введите второе число: '))
        num1 = float(num1)
        if oper == 1:
            print(num1, '+', num2, '=', addition(num1, num2))
        elif oper == 2:
            print(num1, '-', num2, '=', substraction(num1, num2))
        elif oper == 3:
            print(num1, '*', num2, '=', multiplication(num1, num2))
        elif oper == 4:
            print(num1, '/', num2, '=', compertition(num1, num2))
        elif oper == 5:
            print(num1, '//', num2, '=', integer_division(num1, num2))
        elif oper == 6:
            print(num1, '%', num2, '=', seizure_remainder(num1, num2))
        elif oper == 7:
            print(num1, '**', num2, '=', involution(num1, num2))
    elif oper == 8:
        print('Квадратный корень числа ', num1, 'равен', square(int(num1)))
    elif oper == 9:
        bas = int(input('Введите в какой это число системе счисления: '))
        print('Число', num1, 'в десятичной системе будет', intergration(int(num), bas))
    elif oper == 10:
        num1 = int(num1)
        anl = int(input('Введите номер анализа: '))
        if anl == 1:
            x = 1
            num1 //= 10
            while num1 > 0:
                num1 //= 10
                x += 1
            print('В числе', x, 'разряда')
        elif anl == 2:
            if num1 % 2:
                print(num1, 'чётное')
            else:
                print(num1, 'нечётное')
        elif anl == 3:
            summ = 0
            while num1 != 10:
                p = num1 % 10
                summ += p
                num1 //= 10
            print('Сумма цифр числа равна', summ)
        elif anl == 4:
            simple = True
            k = 2
            while k < num1:
                if num1 % k == 0:
                    simple = False
                k += 1
            if simple:
                print('Это чилсо простое')
            else:
                print('Это число сложное')
        elif anl == 5:
            k = 0
            square = False
            while k < num1 and square != True:
                if k * k == num1:
                    square = True
                k += 1
            if square:
                print('Это число является квадратом числа', k)
            else:
                print('Это число не является квадратом')
        elif anl == 6:
            k = 0
            cube = False
            while k < num1 and cube != True:
                if k * k * k == num1:
                    cube = True
                k += 1
            if cube:
                print('Это число является кубом', k)
            else:
                print('Это число не является кубом числа')
    answ = input('Хотите ли продолжить? ')
print('Спасибо за использование калькулятора от Ковалева Степана! Удачи!')
