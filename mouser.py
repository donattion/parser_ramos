import requests
import time

from read_xlsx import read, write, max_rows, save


KEY = '4f470f84-1856-427d-a5c8-98da7e72572c'
BASE_URL = f'https://api.mouser.com/api/v2/search/keyword?apiKey={KEY}'


print('Запуск...')

max_row = max_rows()

for i in range(2920, max_row):
    item = read(i)
    new_product = {
        "SearchByKeywordRequest": {
            "keyword": f"{item}"
        }
    }

    response = requests.post(f"{BASE_URL}", json=new_product)


    try:
        data = response.json()

        category = data['SearchResults']['Parts'][0]['Category']
        manufacturer = data['SearchResults']['Parts'][0]['Manufacturer']
        description = data['SearchResults']['Parts'][0]['Description']
        count = data['SearchResults']['Parts'][0]['ProductAttributes'][-1]['AttributeValue']

        write(symbol='G', number=i, value=category)
        write(symbol='H', number=i, value=manufacturer)
        write(symbol='I', number=i, value=description)
        write(symbol='J', number=i, value=count)


        p = ((i-1)/max_row)*100
        t = (max_row - i-1)*20
        print(i-1, item, category, manufacturer, count, f'; {p} %', f'; осталось: {t} с')
        save()
        time.sleep(20)
    except:
        write(symbol='G', number=i, value='---')

        p = ((i-1)/max_row)*100
        t = (max_row - i-1)*20
        print(i-1, item, '---', f'; {p} %', f'; осталось: {t} с')
        save()
        time.sleep(30)
        continue

print('Завершено!')
