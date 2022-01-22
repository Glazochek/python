"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? Тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма.
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? Постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque, OrderedDict, namedtuple


def haffman_tree(s):

    # вместо Counter я использовал обычный цикл
    # так же, заменил deque на OrderedDict

    sa = {}
    for a in s:
        if a in sa.keys():
            sa[a] += 1
        else:
            sa[a] = 1

    sorted_elements = OrderedDict(sorted(sa.items(), key=lambda item: item[1]))
    se = list(sorted_elements.items())

    if len(se) != 1:
        while len(se) > 1:

            weight = se[0][1] + se[1][1]

            comb = {0: se.pop(0)[0],
                    1: se.pop(0)[0]}

            for i, _count in enumerate(se):
                if weight > _count[1]:
                    continue
                else:
                    se.insert(i, (comb, weight))
                    break
            else:
                se.append((comb, weight))
    else:
        weight = se[0][1]
        comb = {0: se.pop(0)[0], 1: None}
        se.append((comb, weight))
    return se[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


a = "beep boop beer!"
haffman_code(haffman_tree(a))

for i in a:
    print(code_table[i], end=' ')
