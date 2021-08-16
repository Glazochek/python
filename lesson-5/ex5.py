#оптимизация кода по скорости
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def d1(list):
    result = []
    for l in list:
        if list.count(l) == 1:
            result.append(l)
    return result

print(d1(src))

#оптимизация по памяти

def d2(list):
    for l in list:
        if list.count(l) == 1:
            yield l

a = d2(src)
print(a)
print(next(a))
print(next(a))
print(next(a))
