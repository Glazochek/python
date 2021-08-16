#1
def num_translate(number):
    english = { 'one':'один', 'two': 'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight': 'восемь', 'nine': 'девять', 'ten':'десять' }
    print(english.get(number))
num_translate('three')

