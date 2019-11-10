from urllib.request import *
from bs4 import BeautifulSoup as bs

response = urlopen("https://imdb.com")
html = bs(response, 'lxml')
images = html.find_all('img')
# print(len(images))
for image in images:
    # print(image['src'])
    pass

for i in range(len(images)):
    url = images[i]['src']
    fileName = f"{i + 1}.{url[-3:]}"
    urlretrieve(url, fileName)