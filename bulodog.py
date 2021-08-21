#1
second = int(input('Введите колличество секунд:     '))

point = ':'
minute = second // 60
second = second % 60
hour = minute // 60
minute = minute - hour * 60
day = hour // 24
hour = hour - day * 24

print(day, point, hour, point, minute, point, second)

#2
number_list = []
for i in range(0, 100):
    if i%2 != 0:
        print(i)
        i = i**3
        number_list.append(i)
print(number_list)


#3
procent = str(input('Введите колличество процентов      '))
last_number = (procent)[-1]

if last_number == '2':
    print(procent, 'процента')
elif last_number == '3':
    print(procent, 'процента')
elif last_number == '4':
    print(procent, 'процента')
elif last_number == '1':
    print(procent, 'процент' )
else:
    print(procent, 'процентов')