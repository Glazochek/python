#1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#2
list_information = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_information_2 = []

for li in list_information:
    if li.isdigit():
        if len(li) == 1:
            li = '0' + li
            list_information_2.append(li)
        elif len(li) == 2:
            list_information_2.append(li)

        list_information_2.insert(list_information_2.index(li), ' "')
        list_information_2.insert(list_information_2.index(li) + 1, '" ')
    elif li[0] == '+' and len(li) == 2:
        li = li[0] + '0' + li[-1]
        list_information_2.append(li)
        list_information_2.insert(list_information_2.index(li), '"')
        list_information_2.insert(list_information_2.index(li) + 1, '"')

    else:
        list_information_2.append(li)

str_li_2 = ' '.join(list_information_2)
print(str_li_2)

#4
list_worker = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
list_rekrow = []
list_name = []

for lw in list_worker:
    list_rekrow.append(lw[::-1])
print(list_rekrow)

for lr in list_rekrow:
    index = lr.find(' ')
    print(index)
    list_name.append(lr[:index])
print(list_name)

for ln in list_name:
    print('Привет,',  ln[::-1], '!')

#5
price = [5.7, 45.18, 97, 54, 34.6, 67.32]

def money(numbers):
    price_str = []
    for num in numbers:
        p_str = str(num)
        price_str.append(p_str)
    for number in price_str:
        index = number.find('.')
        kk = number[index+1:]
        if index == -1:
            kk = '00'
            index = None
        elif len(number[index+1:]) == 1:
            kk = '0' + number[index+1:]

        print('   ', number[:index], 'руб', kk, 'коп')

money(price)
print('______по убыванию_______')
price_min = [money(sorted(price))]
print('______по возростанию_______')
price_max = [money(sorted(price, reverse=True))]
print('_______топ 5 цен________')
money(sorted(price[:5], reverse=True))
print('_______________________')
