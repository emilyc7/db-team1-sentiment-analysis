# This function will handle all calls and passing of information
# =============================================================================
# import Web2String
# import WebCrawler
# import company_identifier
# import StockTest
# import evaluate_NN
# =============================================================================
import json
def main(url):
# =============================================================================
#     string = Web2String.url2string(url)
#     entity = company_identifier.entity(string)
#     # ticker = company_identifier.find_ticker(entity)
#     other_articles = WebCrawler.getArticles(entity) # array of article urls
#     StockTest.stockGraph(entity)
#     
#     # print(string)
#     main_article_sentiment = evaluate_NN.evaluate_NN(string)  # analyze sentiment of main article
# 
#     # arrays that will hold similar/different articles and their sentiments
#     other_article_sentiment = []
# 
#     for x in range(len(other_articles)):
#         curr_article = Web2String.url2string(other_articles[x])
# 
#         # analyze sentiment of article and put in array
#         other_article_sentiment[x] = evaluate_NN.evaluate_NN(curr_article)
#         # other_article_sentiment.append(evaluate_NN.evaluate_NN(curr_article))
#     # print(entity)
#     return main_article_sentiment*10
# 
# =============================================================================
    # return other_articles (list of urls), other_article_sentiment (list of sentiments), main_article_sentiment (original article's sentiment), entity (company name), ticker data (csv)
# =============================================================================
#     other_articles = [ "sampleOne.com", "sampleTwo.com", "sampleThree.com", "sampleFour.com", "sampleFive.com" ]
#     other_article_sentiment = [1, 2, 3, 4, 5]
#     main_article_sentiment = 10
#     entity = "Deutsche Bank"
# =============================================================================
    
    other_articles_dict = { 'other_articles' : { 'one' : 'sampleOne.com', 'two' : 'sampleTwo.com', 'three' : 'sampleThree.com', 'four' : 'sampleFour.com', 'five' : 'sampleFive.com' }}
    other_article_sentiment_dict = { 'other_articles_sentiment' : { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5 }}
    main_article_sentiment_dict = { 'main_article_sentiment' : 10 }
    entity_dict = { 'company_name' : 'Deutsche Bank' }
    
    rv = {}
    
    rv.update(other_articles_dict)
    rv.update(other_article_sentiment_dict)
    rv.update(main_article_sentiment_dict)
    rv.update(entity_dict)
    
    rv_json = json.dumps(rv)
    
    return rv_json
# main('https://www.reuters.com/article/us-apple-services-research/apples-services-revenue-china-to-power-third-quarter-analyst-idUSKCN1U40SH')
