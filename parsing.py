import requests
from bs4 import BeautifulSoup as BS
import time

from read_xlsx import read, write, max_rows, save


header = {
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'accept-encoding':'gzip, deflate, br',
  'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control':'no-cache',
  'dnt': '1',
  'pragma': 'no-cache',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

session = requests.Session()
session.headers = header

max_row = max_rows()

for i in range(2, 150):
    value = read(i)
    url = f'https://www.icsource.ru/productdetail/{value}'
    r = session.get(url)
    html = BS(r.content, 'html.parser')

    s = '---'
    for el in html.select('.breadcrumb'):
        title =el.select('a')
        #s = ' '.join(map(str, title[0].text.split('«')[1::1]))
        #s = s.translate(str.maketrans('«', ' ', string.punctuation))
        #s = s.translate(str.maketrans('»', ' ', string.punctuation))
        s = title[2].text
        write(number=i, value=s)

    print(i, value, s)
    save()
    time.sleep(15)

print('Завершено!')


