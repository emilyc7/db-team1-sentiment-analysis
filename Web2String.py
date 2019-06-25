# import nltk
# import urllib
import requests
from bs4 import BeautifulSoup
#import company_identifier

# downloads url and converts to a HTML
webURL = requests.get('https://www.forbes.com/sites/kenkam/2019/06/25/tesla-beating-competitors-even-with-its-hands-tied/#72f8c1041d8f')
soup = BeautifulSoup(webURL.content, 'html.parser')

# Loops through all the instances with a <p> tag and prints them
y = soup.find_all('p')
z = 0
for x in y:
    a = soup.find_all('p')[z].get_text()
    print(a)
    z += 1












