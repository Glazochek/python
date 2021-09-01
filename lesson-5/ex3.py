tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Анастасия', 'Петр', 'Сергей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def T_and_K(tutors, klasses):
    index = 0
    for tut in tutors:
        l = []
        if index > len(klasses)-1:
            klas = None
        else:
            klas = klasses[index]
        l.append(tut)
        l.append(klas)
        index += 1
        yield tuple(l)

kt = T_and_K(tutors, klasses)
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
print(next(kt))
