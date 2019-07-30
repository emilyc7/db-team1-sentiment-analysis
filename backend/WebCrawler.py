# from newsapi import NewsApiClient
import datetime
import urllib
from newsapi.newsapi_client import NewsApiClient


def getInfo(query):
    #Key to access GoogleNews API
    query = query.lower()
    # query = urllib.parse.quote_plus(query)
    newsapi = NewsApiClient(api_key='edf0afe93d6644d198d8539e640134c9')
    # print(query)

    headlines = newsapi.get_top_headlines(q=query, language='en')
    # print(headlines)
    # headlines = newsapi.get_top_headlines(q=query, language='en')

    newsTitles = list()
    newsContent = list()
    newsSources = list()
    newsURL = list()
    # print("number of articles found = " + str(len(headlines['articles'])))

    #Adds all relevant information to separate lists
    numberOfArticles = len(headlines['articles'])
    if numberOfArticles > 5:
        numberOfArticles = 5
    for x in range(numberOfArticles):
        # source = newsSources.append(headlines['articles'][x]['source']['name'])
        # if source == "Google News" or source == "Reuters":
        #    print(source)
        #    x -= 1
        #    continue
        newsTitles.append(headlines['articles'][x]['title'])
        newsContent.append(headlines['articles'][x]['content'])
        newsSources.append(headlines['articles'][x]['source']['name'])
        newsURL.append(headlines['articles'][x]['url'])

    if len(newsTitles) < 5:
        today = datetime.datetime.today()
        start_day = today - datetime.timedelta(days=1)
        headlines_all = newsapi.get_everything(q=query, from_param=str(start_day), to=str(today), language='en',
                                               sort_by='relevancy')
        for x in range(5 - len(newsTitles)):
            # source = newsSources.append(headlines_all['articles'][x]['source']['name'])
            # if source == "Google News" or source == "Reuters":
            #    print(source)
            #    x -= 1
            #    continue

            newsTitles.append(headlines_all['articles'][x]['title'])
            newsContent.append(headlines_all['articles'][x]['content'])
            newsSources.append(headlines_all['articles'][x]['source']['name'])
            newsURL.append(headlines_all['articles'][x]['url'])

    return newsTitles, newsContent, newsSources, newsURL

