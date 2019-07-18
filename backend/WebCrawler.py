from GoogleNews import GoogleNews


# returns a list of 5 articles related to the query
def getArticles(query):
    googlenews = GoogleNews()
    googlenews.search(query)
    x = googlenews.getlinks()
    return x
