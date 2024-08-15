import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'

qHeader = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

qResp = rq.get(url=qUrl, headers= qHeader)

bSoup = BeautifulSoup(qResp.content, 'html.parser')

def removeNavigableString(value):
    return list(filter(lambda x: type(x) != NavigableString, value))

c = removeNavigableString(bSoup.ol.children)
t1 = (c[4].h3.a.attrs['title'])

t2 = (c[5].h3.a.attrs['title'])

t3 = (c[6].h3.a.attrs['title'])

t4 = (c[7].h3.a.attrs['title'])

print("2 row titles :")

print('Title 1 : ',t1)
print('Title 2 : ',t2)
print('Title 3 : ',t3)
print('Title 4: ', t4)

