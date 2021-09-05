import os
def funk(papka):
    size = [100, 1000, 10000, 100000]
    stat = {}
    for s in size:
        stat[s] = None
    ola = os.path.abspath(papka)
    ol = [f for f in os.listdir(ola) if os.path.isfile(os.path.join(ola, f))]
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for o in ol:
        if os.path.exists(o):
            siz = os.path.getsize(o)
            if siz <= 100:
                count1 = count1 + 1
            elif siz <= 1000 and siz > 100:
                count2 = count2 + 1
            elif siz > 1000 and siz <= 10000:
                count3 = count3 + 1
            elif siz > 10000:
                count4 = count4 + 1
    stat[100] = count1
    stat[1000] = count2
    stat[10000] = count3
    stat[100000] = count4
    return stat
