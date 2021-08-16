def num_translate(number):
    english = { 'One':'Один', 'Two': 'Два', 'Three':'Три', 'Four':'Четыре', 'Five':'Пять', 'Six':'Шесть', 'Seven':'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten':'Десять',
               'one':'один', 'two': 'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight': 'восемь', 'nine': 'девять', 'ten':'десять' }
    print(english.get(number))
num_translate('three')

