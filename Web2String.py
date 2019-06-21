import nltk
import urllib
import requests
from bs4 import BeautifulSoup

#downloads url and converts to a HTML
webURL = requests.get('https://finance.yahoo.com/news/deutsche-bank-db-continues-overhauling-113311379.html')
soup = BeautifulSoup(webURL.content, 'html.parser')

#Gets only the text in string form under <body> tag of HTML
x = soup.find_all('p')[0].get_text()

#Just to test that it works
print(x)









