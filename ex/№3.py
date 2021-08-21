def thesaurus(*name):
    ls={}
    for lis in name:
        n = lis[0]
        if n not in ls:
            ls[n] = []
        ls[n].append(lis)
    return ls
print(thesaurus("Иван", "Мария", "Петр", "Илья"))


