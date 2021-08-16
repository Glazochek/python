#2,3

def currency_rates(currency):
    from requests import get
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    currency_valuable = {}
    date = content.split('Date="')[1].split('" name')[0]
    for el in content.split('ID="')[1:]:
        Value = float(el.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
        CharCode = el.split('<CharCode>')[1].split('</CharCode>')[0]
        currency_valuable[CharCode] = Value

    return print(currency_valuable.get(currency),',', date)

if __name__ == '__main__':
    currency_rates('EUR')
    currency_rates('USD')
    currency_rates('MDL')