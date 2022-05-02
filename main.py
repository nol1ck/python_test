import requests
from bs4 import BeautifulSoup as BS


r = requests.get('https://stopgame.ru/review/new/izumitelno/p1')
html = BS(r.content, 'html.parser')


