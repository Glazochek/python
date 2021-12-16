"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. Решение через цикл не принимается.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def cn(number, ch = 0, nch = 0):
    n = len(str(number)) - 1
    if ch == 0:
        if str(number).find('0') != -1:
            ch += 1

    if (number // 10**n) % 2 == 0:
        ch += 1

    elif (number // 10**n) % 2 != 0:
        nch += 1

    if len(str(number)) <= 1:
        print((ch, nch))
        return ''

    cn(number - (number // 10**n) * 10**n, ch, nch)

cn(12305)


