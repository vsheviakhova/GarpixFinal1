import requests
from bs4 import BeautifulSoup

url = 'https://stopgame.ru/news/all/p1'

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
# использую библиотеку BeautifulSoup, потому что нашла это решение в интернете)
link = soup.find('div', class_="item article-summary").\
    find('a', class_='article-image').\
    find('img').get('src')

# нахожу ссылку на одну картинку

links = soup.findAll('div', class_="item article-summary")


# в цикле записываю каждую картинку в отдельный файл и кладу ее в images
counter = 1
for i in links:
    i = i.find('a', class_='article-image').find('img').get('src')
    response = requests.get(i)
    filename = f'pic{counter}.jpg'
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)
    print(counter)  # можно и не отсчитывать, но так было в вашем видео :)
    counter += 1
