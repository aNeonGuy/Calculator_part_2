print('Здраствуйте, пользователь! Это калькулятор, он умеет:')
print(' - сложение(1)') #начало/start
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
    x = str(x)
    base = int(base)
    try:
        return int(x, base)
    except ValueError:
        return None


def parts(x):
    part = 1
    x //= 10
    while x > 0:
        x //= 10
        part += 1
    return part


def even_odd(x):
    if x % 2 == 0:
        return 'чётное'
    return 'нечётное'


def sum_parts(x):
    summ = 0
    while x != 10:
        p = x % 10
        summ += p
        x //= 10
        return summ

def simp(x):
    simple = True
    k = 2
    while k < x:
        if x % k == 0:
            simple = False
            break
        k += 1
    if simple:
        return 'простое'
    return 'сложное'


def square(x):
    k = 0
    square = False
    while k < x and not square:
        if k ** 2 == x:
            square = True
            break
        k += 1
    if square:
        return k
    return None


def cube(x):
    k = 0
    cubert = False
    while k < x and not cubert:
        if k ** 3 == x:
            cube = True
            break
        k += 1
    if cube:
        return k
    return None


while answ:
    num1 = input('Введите первое число: ') #середина/middle
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
        if intergration(int(num), bas) == None:
            print('Это число не из этой системы счисления')
    elif oper == 10:
        num1 = int(num1)
        anl = int(input('Введите номер анализа: '))
        if anl == 1:
            print('В числе', parts(num1), 'разряда')
        elif anl == 2:
            print(num1, '-', even_odd(num1))
        elif anl == 3:
            print('Сумма цифр числа равна', sum_parts(num1))
        elif anl == 4:
            print('Это число', simp(num1))
        elif anl == 5:
            if square(num1) == None:
                print('Не является квадратом')
            else:
                print('Это число является квадратом числа', square(num1))
        elif anl == 6:
            if cube(num1) == None:
                print('Не является квадратом')
            else:
                print('Это число является кубом', cube(num1))
    answ = input('Хотите ли продолжить? ')
print('Спасибо за использование калькулятора от Ковалева Степана! Удачи!') #конец/end
