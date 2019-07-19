# from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient

def getInfo(query):
    #Key to access GoogleNews API
    newsapi = NewsApiClient(api_key='edf0afe93d6644d198d8539e640134c9')
    #query
    headlines = newsapi.get_top_headlines(q=query)
    newsTitles = list()
    newsContent = list()
    newsSources = list()
    newsURL = list()
    #Adds all relevant information to separate lists
    for x in range(5):
        newsTitles.append(headlines['articles'][x]['title'])
        newsContent.append(headlines['articles'][x]['content'])
        newsSources.append(headlines['articles'][x]['source']['name'])
        newsURL.append(headlines['articles'][x]['url'])
    return newsTitles, newsContent, newsSources, newsURL




