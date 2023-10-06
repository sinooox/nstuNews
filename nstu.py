import requests
from bs4 import BeautifulSoup

lst = []
pages = 3

for page in range(1, pages+1):
    mainURL = f'https://www.nstu.ru/news/?page={page}'
    response = requests.get(mainURL)
    soup = BeautifulSoup(response.text, 'lxml')
    news = soup.find_all('div', class_='bottomLine')
    for post in news:
        url = post.select('a')[1]
        title = url.text
        link = url['href']
        newsID = int(link[link.find('=')+1:-1])
        lst.append({'title':title, 'id':newsID, 'link':link})
        print(f"{title}\n{newsID}")
        print('-'*30)

for i in lst:
    print(i)
