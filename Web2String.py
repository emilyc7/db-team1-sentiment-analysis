import requests
from bs4 import BeautifulSoup


# takes string of url as input and returns content of website in string format
def url2string(url):
    # downloads url and converts to a HTML
    webURL = requests.get(url)
    soup = BeautifulSoup(webURL.content, 'html.parser')

    # Loops through all the instances with a <p> tag and prints them
    y = soup.find_all('p')
    z = 0
    b = ""
    for x in y:
        a = soup.find_all('p')[z].get_text()
        b += a
        z += 1

    return b
