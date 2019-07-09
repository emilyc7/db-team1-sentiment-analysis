# This function will handle all calls and passing of information
import Web2String
import WebCrawler
import company_identifier
import StockTest
import evaluate_NN


def main(url):
    string = Web2String.url2string(url)
    entity = company_identifier.entity(string)
    # ticker = company_identifier.find_ticker(entity)
    other_articles = WebCrawler.getArticles(entity)
    StockTest.stockGraph(entity)

    main_article_sentiment = evaluate_NN.evaluate_NN(string)  # analyze sentiment of main article
    low_range = main_article_sentiment - 0.1
    high_range = main_article_sentiment + 0.1

    # arrays that will hold similar/different articles and their sentiments
    same_article = []
    different_article = []
    same_sentiment = []
    different_sentiment = []

    same_count = 0
    different_count = 0

    for x in range(len(other_articles)):
        curr_article = Web2String.url2string(other_articles[x])

        # analyze sentiment of article
        curr_article_sentiment = evaluate_NN.evaluate_NN(curr_article)

        # if sentiment is within threshold, add to same_sentiment
        if low_range <= curr_article_sentiment <= high_range:
            same_article[same_count] = curr_article
            same_sentiment[same_count] = curr_article_sentiment
            same_count += 1
        else:
            different_article[different_count] = curr_article
            different_sentiment[different_count] = curr_article_sentiment
            different_count += 1


main('https://www.cnbc.com/2019/07/08/axed-deutsche-bank-workers-leave-offices-en-masse-belongings-in-hand.html')
