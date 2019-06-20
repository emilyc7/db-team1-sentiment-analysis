import nltk
import urllib
import requests
from bs4 import BeautifulSoup


webURL = requests.get('https://finance.yahoo.com/news/deutsche-bank-db-continues-overhauling-113311379.html')
soup = BeautifulSoup(webURL.content, 'html.parser')
x = soup.find_all('p')[0].get_text()
print(x)









