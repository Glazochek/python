from termcolor import colored


class NumEror(ValueError):
    only_num = []
    print('Если хотите остановить цикл, напишите "stop"')
    while True:
        n = input('Введите только число ')
        if n == 'stop':
            break
        try:
            only_num.append(int(n))
        except ValueError:
            print(colored(f'"{n}" - ЭТО НЕ ЧИСЛО!', 'red'))
    print(only_num)
