def thesaurus_adv(*name):
    ls={}
    for lis in name:
        listik = list(lis)
        index = listik.index(' ')
        b = lis[index+1]
        n = lis[0]
        if b not in ls:
            ls[b] = {}
        if n not in ls[b]:
            ls[b][n] = []

        ls[b][n].append(lis)
    return ls

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Иавельева"))

