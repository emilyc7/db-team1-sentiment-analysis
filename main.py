# This function will handle all calls and passing of information
import Web2String
import WebCrawler
import company_identifier
import StockTest


def main(url):
    string = Web2String.url2string(url)
    entity = company_identifier.entity(string)
    # ticker = company_identifier.find_ticker(entity)
    other_articles = WebCrawler.getArticles(entity)
    # ML(string) and other articles

