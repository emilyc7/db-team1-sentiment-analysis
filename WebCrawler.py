from googlesearch import search
from GoogleNews import GoogleNews

query = "amazon"
googlenews = GoogleNews()

googlenews.search(query)
x = googlenews.getlinks()
print(x)
# for x in search(query, tld='com', lang='en', num=10, stop=5, pause=2):
#   print(x)
