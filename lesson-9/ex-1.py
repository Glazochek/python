def email_parse(email):
    sl = {}
    try:
        index = email.index('@')
        index_two = email.index('.') # здесь я поставил точку, что бы если почта введена без точки была ошибка
        sl['username'] = email[:index]
        sl['domain'] = email[index+1:]
        return sl
    except (ValueError, UnboundLocalError):
        print(f'ValueError: wrong email: {email}')
        return 'Введи свою электронную почту правильно'

print(email_parse('an9680411@gmail.com'))