#3

import csv, sys
users = {}
hobby_users = {}

with open('users.csv', mode='w', encoding='utf-8') as file:
    file_write = csv.writer(file, delimiter=',', lineterminator='\r')
    file_write.writerow(['Афанасьев','Никита','Алексеевич'])
    file_write.writerow(['Иванов','Иван','Иванович'])
    file_write.writerow(['Петров','Петр','Петрович'])
with open('users.csv',encoding='utf-8') as file:
    file_read = csv.reader(file, delimiter=',')
    for row in file_read:
        hobby_users[str(row)] = None

with open('hobby.csv', mode='w', encoding='utf-8') as file:
    file_write = csv.writer(file, delimiter=',', lineterminator='\r')
    file_write.writerow(['скалолазание охота'])
    file_write.writerow(['горные лыжи'])
hobby = []
index = 0
with open('hobby.csv', mode='r', encoding='utf-8') as file:
    file_read = csv.reader(file, delimiter=',')
    for row in file_read:
        hobby.append(row)

for key in hobby_users.keys():
    if len(hobby) - 1 < index:
        hobby_users[key] = None
    else:
        hobby_users[key] = hobby[index]
        index += 1

with open('hobby_users.csv', mode='w+', encoding='utf-8') as file:
    file_write = csv.writer(file, delimiter=',', lineterminator='\r')
    for key ,value in hobby_users.items():
        kv = f'{key}:{value}'
        file_write.writerow([f"{kv}\n"])
        if key == None:
            sys.exit(1)
