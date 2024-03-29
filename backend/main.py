# This function will handle all calls and passing of information
import Web2String
import WebCrawler
import company_identifier
import StockTest
import evaluate_NN
import summary
import StockToPython
import json


def main(url):
    string = Web2String.url2string(url)
    print(string)
    entity = company_identifier.entity(string)
    print(entity)
    newsTitles, newsContent, newsSources, other_articles_URL = WebCrawler.getInfo(entity)  # array of article urls

    # main URL summary 
    main_summary = summary.summary(url)
    print(main_summary)
    
    print(newsTitles)
    # print(string)
    main_article_sentiment = round(evaluate_NN.evaluate_NN(string)*100)  # analyze sentiment of main article
    print(main_article_sentiment)
    # arrays that will hold similar/different articles and their sentiments
    other_article_sentiment = list()
# 
    for x in range(len(other_articles_URL)):
        curr_article = Web2String.url2string(other_articles_URL[x])
        # analyze sentiment of article and put in array
        other_article_sentiment.append(round(evaluate_NN.evaluate_NN(curr_article)*100))

    a_summary = list()
    for x in range(len(other_articles_URL)): 
        a_summary.append(summary.summary(other_articles_URL[x]))

    stock_dates, stock_data = StockToPython.stock_to_JSON(entity)

    other_articles_titles_dict = {'other_articles_titles': {'one':      newsTitles[0],
                                                            'two':      newsTitles[1],
                                                            'three':    newsTitles[2],
                                                            'four':     newsTitles[3],
                                                            'five':     newsTitles[4]}}
    other_articles_sources_dict = {'other_articles_sources': {'one':    newsSources[0],
                                                              'two':    newsSources[1],
                                                              'three':  newsSources[2],
                                                              'four':   newsSources[3],
                                                              'five':   newsSources[4]}}
    other_articles_sentiment_dict = {'other_articles_sentiment': {'one':     other_article_sentiment[0],
                                                                  'two':     other_article_sentiment[1],
                                                                  'three':   other_article_sentiment[2],
                                                                  'four':    other_article_sentiment[3],
                                                                  'five':    other_article_sentiment[4]}}
    other_articles_links_dict = {'other_articles_links': {'one':    other_articles_URL[0],
                                                          'two':    other_articles_URL[1],
                                                          'three':  other_articles_URL[2],
                                                          'four':   other_articles_URL[3],
                                                          'five':   other_articles_URL[4]}}
    article_summary = {'article_summary': {'one':   a_summary[0],
                                           'two':   a_summary[1],
                                           'three': a_summary[2],
                                           'four':  a_summary[3],
                                           'five':  a_summary[4]}}
    main_article_sentiment_dict = {'main_article_sentiment': main_article_sentiment}
    entity_dict = {'company_name': entity}
    main_article_summary = {'main_summary': main_summary}
    stock_dates_dict = {'stock_dates': stock_dates}
    stock_data_dict = {'stock_data': stock_data}

    rv = {}

    rv.update(other_articles_titles_dict)
    rv.update(other_articles_sources_dict)
    rv.update(other_articles_sentiment_dict)
    rv.update(other_articles_links_dict)
    rv.update(main_article_sentiment_dict)
    rv.update(entity_dict)
    rv.update(article_summary)
    rv.update(main_article_summary)
    rv.update(stock_dates_dict)
    rv.update(stock_data_dict)

    rv_json = json.dumps(rv)
    print(rv_json)
    return rv_json

# main('https://www.cnet.com/news/apples-q3-earnings-are-all-about-the-iphone-11-hints/')