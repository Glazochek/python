from termcolor import colored


class ZeroError(ZeroDivisionError):
    num_1 = input('Введите первое число  ')
    num_2 = input('Введите второе число  ')
    try:
        ex = int(num_1) / int(num_2)
    except ZeroDivisionError:
        print(colored('ErorZero: Нельзя делить на ноль! ', 'red'))
    else:
        print(ex)


ze = ZeroError()
print(ze)