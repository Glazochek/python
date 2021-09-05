import csv
import sys
with open('bakery.csv', mode='w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter=',', lineterminator='\r')
    write.writerow([1, 5978.5])
    write.writerow([2, 8914.3])
    write.writerow([3, 7879.1])
    write.writerow([4, 1573.7])

sells = []
with open('bakery.csv', 'r', encoding='UTF-8') as file:
    for line in file:
        sells.append(line[:-1])

def sell(*s):
    pp = []
    for sel in sells:
        for ss in s:
            if str(ss) == sel[0]:
                p = sel[2:]
                pp.append(p)
    if len(s) == 0:
        pp = sells
    return str(pp)

for ech in sys.argv[1:]:
   print(sell(ech))