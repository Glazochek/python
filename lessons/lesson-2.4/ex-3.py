"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit

nm = 12345


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    a = list(str(enter_num))
    a.reverse()
    return ''.join(a)


print(timeit('revers(nm)', setup='from __main__ import revers, nm', number=10000), '- revers - 4')
print(timeit('revers_2(nm)', setup='from __main__ import revers_2, nm', number=10000), '- revers_2 - 3')
print(timeit('revers_3(nm)', setup='from __main__ import revers_3, nm', number=10000), '- revers_3 - 1')
print(timeit('revers_4(nm)', setup='from __main__ import revers_4, nm', number=10000), '- revers_4 - 2')

# 0.009803096 - revers - 4
# 0.006115842 - revers_2 - 3
# 0.002418631999999997 - revers_3 - 1
# 0.003946383000000005 - revers_4 - 2

# быстрее всех оказалась функция revers_3, в ней используется срез, который обладает линейной сложностью
# в остальных функциях используется давольно сложные операции
