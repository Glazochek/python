from pympler import asizeof
from recordclass import recordclass
# Основы языка Python: урок 8 задание 1


def email_parse(email):
    sl = {}
    try:
        index = email.index('@')
        sl['username'] = email[:index]
        sl['domain'] = email[index+1:]
        return sl
    except (ValueError, UnboundLocalError):
        print(f'ValueError: wrong email: {email}')
        return 'Введи свою электронную почту правильно'


def email_parse_2(email):
    try:
        index = email.index('@')
        point = recordclass('Point', 'username domain')
        p = point(email[:index], email[index+1:])
        del index
        return p
    except (ValueError, UnboundLocalError):
        print(f'ValueError: wrong email: {email}')
        return 'Введи свою электронную почту правильно'


print(asizeof.asizeof(email_parse('an968041@gmail.com')))  # 480
print(asizeof.asizeof(email_parse_2('an968041@gmail.com')))  # 32
# результат просто отличный, я использовал 'recordclass' вместо словаря
print(email_parse('an968041@gmail.com'))
print(email_parse_2('an968041@gmail.com'))
