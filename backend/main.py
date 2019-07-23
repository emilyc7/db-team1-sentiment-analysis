# This function will handle all calls and passing of information
# =============================================================================
import Web2String
import WebCrawler
import company_identifier
import StockTest
import evaluate_NN
import summary
# =============================================================================
import json


def main(url):
    string = Web2String.url2string(url)
    print(string)
    entity = company_identifier.entity(string)
    print(entity)
    # ticker = company_identifier.find_ticker(entity)
    newsTitles, newsContent, newsSources, other_articles_URL = WebCrawler.getInfo(entity)  # array of article urls

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
        # other_article_sentiment[x] = round(evaluate_NN.evaluate_NN(curr_article)*100)
        other_article_sentiment.append(round(evaluate_NN.evaluate_NN(curr_article)*100))
    # print(entity)
#     return main_article_sentiment*10
# 

    for x in range(len(other_articles_URL)): 
        a_summary = summary.summary(other_articles_URL)
# =============================================================================
    # return other_articles (list of urls), other_article_sentiment (list of sentiments), main_article_sentiment (original article's sentiment), entity (company name), ticker data (csv)
# =============================================================================
#     other_articles = [ "sampleOne.com", "sampleTwo.com", "sampleThree.com", "sampleFour.com", "sampleFive.com" ]
#     other_article_sentiment = [1, 2, 3, 4, 5]
#     main_article_sentiment = 10
#     entity = "Deutsche Bank"
# =============================================================================
    
    other_articles_titles_dict = {'other_articles_titles': {'one': newsTitles[0],
                                                            'two': newsTitles[1],
                                                            'three': newsTitles[2],
                                                            'four': newsTitles[3],
                                                            'five': newsTitles[4]}}
    other_article_sentiment_dict = {'other_articles_sentiment': {'one': other_article_sentiment[0],
                                                                 'two': other_article_sentiment[1],
                                                                 'three': other_article_sentiment[2],
                                                                 'four': other_article_sentiment[3],
                                                                 'five': other_article_sentiment[4]}}
    article_summary = {'article_summary' : { 'one' : a_summary[0],
                                            'two': a_summary[1],
                                            'three': a_summary[2],
                                            'four': a_summary[3], 
                                            'five': a_summary[4] }} 
    main_article_sentiment_dict = {'main_article_sentiment': main_article_sentiment}
    entity_dict = {'company_name': entity}
    
    rv = {}
    
    rv.update(other_articles_titles_dict)
    rv.update(other_article_sentiment_dict)
    rv.update(main_article_sentiment_dict)
    rv.update(entity_dict)
    rv.update(article_summary)
    
    rv_json = json.dumps(rv)
    
    return rv_json
# main('https://www.reuters.com/article/us-apple-services-research/apples-services-revenue-china-to-power-third-quarter-analyst-idUSKCN1U40SH')
