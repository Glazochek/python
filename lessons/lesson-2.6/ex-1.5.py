from pympler import asizeof

# Алгоритмы и структуры данных на Python: урок 4 задание 3

array = [1, 3, 3, 2, 4, 5, 2, 1, 3, 3]


# было
def func_1():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    mx = max(new_array)
    elem = array[new_array.index(mx)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {mx} раз(а)'


# стало
def func_2():
    for n in tuple((el, array.count(el)) for el in array):
        if n[1] == max(map(array.count, array)):
            return f'Чаще встречается {n[0]} оно появилось {n[1]} раз'


print(asizeof.asizeof(func_1()))  # 208
print(asizeof.asizeof(func_2()))  # 152

#  столько всего сделал
#  например сделал генератор и воспользовался функцией map
