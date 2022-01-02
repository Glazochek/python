from pympler import asizeof
# Основы языка Python: урок 1 задание 2


def tg():
    number_list = []
    for i in range(0, 10000):
        if i % 2 != 0:
            i = i ** 3
            number_list.append(i)
    return number_list


def tg1():
    return (i**3 for i in range(0, 10000) if i % 2 != 0)


print(asizeof.asizeof(tg()))  # 201880
print(asizeof.asizeof(tg1()))  # 432
# использовал генератор
