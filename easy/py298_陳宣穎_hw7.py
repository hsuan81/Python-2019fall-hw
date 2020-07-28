import pip
import requests
from bs4 import BeautifulSoup as bs
r = requests.get('https://movies.yahoo.com.tw/movieinfo_main/%E6%AF%8F%E5%A4%A9%E5%9B%9E%E5%AE%B6%E8%80%81%E5%A9%86%E9%83%BD%E5%9C%A8%E8%A3%9D%E6%AD%BB-when-i-get-home-my-wife-always-pretends-to-be-dead-8153')
html = r.content.decode('utf8')
soup = bs(html, 'html.parser')
a = soup.find('h1')
print('電影名稱:',a.string)
b = soup.find('h3')
print(b.string)
c = soup.find('a',attrs = {'class': 'gabtn','href':'https://movies.yahoo.com.tw/moviegenre_result.html?genre_id=10'})
c1 = soup.find('a',attrs = {'class': 'gabtn','href':'https://movies.yahoo.com.tw/moviegenre_result.html?genre_id=09'})

#type of movie
print('類型:')
print(c.string, c1.string)
d = soup.select('div.movie_intro_info_r > span', limit=3)
#select找出的為list type, pick out items in list later
for item in d:
    print(item.string)
e = soup.find('div','movie_intro_list')
#director
print('導演:', e.string)
f = soup.find('a', attrs = {'class': 'gabtn','href':'https://movies.yahoo.com.tw/name_main/%E6%A6%AE%E5%80%89%E5%A5%88%E5%A5%88-nana-eikura-1266'})
#actors
print('演員:', f.string)
g = soup.find('a',href="https://www.facebook.com/garageplay.tw")
#website1
h = soup.find('a',href="http://garageplay.tw/")
#website2
print('官網:', '\n',g.string,'\n', h.string)


