from pympler import asizeof

# Основы языка Python: урок 3 задание 3


# было
def thesaurus(*name):
    ls = {}
    for lis in name:
        n = lis[0]
        if n not in ls:
            ls[n] = []
        ls[n].append(lis)
    return ls


# стало
def thesaurus_2(*name):
    ls = {}
    for lis in name:
        if lis[0] not in ls:
            ls[lis[0]] = [lis]
    return ls


print(asizeof.asizeof(thesaurus('ffr')))  # 432
print(asizeof.asizeof(thesaurus_2('ffr')))  # 408
# не самый худший результат
# убрал лишние ярлыки
print(thesaurus('ffr'))
print(thesaurus_2('ffr'))
