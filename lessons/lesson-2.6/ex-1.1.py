from pympler import asizeof
from sys import getsizeof

# Основы языка Python: урок 3 задание 3


# было
def thesaurus(*name):
    lls = {}
    for lis in name:
        n = lis[0]
        if n not in lls:
            lls[n] = []
        lls[n].append(lis)
    return lls


# стало
ls = {}


def thesaurus_2(lss, *name):
    for lis in name:
        if lis[0] not in lss:
            lss[lis[0]] = [lis]
    return lss


print(asizeof.asizeof(thesaurus('ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr',
                                'ffr', 'ffr')))
# 432
print(asizeof.asizeof(thesaurus_2(ls, 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr',
                                  'ffr', 'ffr', 'ffr')))
# 408

print(getsizeof(thesaurus('ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr',
                          'ffr', 'ffr', 'ffr', 'ffr')))
# 432
print(getsizeof(thesaurus_2('ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr', 'ffr',
                            'ffr', 'ffr', 'ffr', 'ffr')))

# в первой функции я отдельно ключам присваивал списки, а потом уже дабовлял в них аргументы
# во второй делаю все сразу

# не самый худший результат
# убрал лишние ярлык: n
# так же, вынес отдельно словарь (ls)
