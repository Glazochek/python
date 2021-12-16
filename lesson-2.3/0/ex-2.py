"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами да нных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib
import os

pwd = '123'  # это пароль!!!!!!!!
salt = os.urandom(32)


def pwd_to_hash(psd):
    return hashlib.pbkdf2_hmac('sha256', psd.encode('utf-8'), salt, 1000)


keyword = pwd_to_hash(pwd)
hsh = {pwd: keyword}
password = input()


try:
    if pwd_to_hash(password) == hsh[password]:
        print('1) пароль верный!')
        password = input()
        if pwd_to_hash(password) == hsh[password]:
            print('2) пароль верный!')
except KeyError:
    print('неверный пароль')
