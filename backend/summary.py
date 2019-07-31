import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


def summary(url):
    page = requests.get(url).text

    soup = BeautifulSoup(page, features="lxml")
    
    p_tags = soup.find_all('p') 
    p_tags_text = [tag.get_text().strip() for tag in p_tags]

    # sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in p_tags_text if '.' in sentence]
    # sentence_list = [sentence for sentence in sentence_list if not '-' in sentence]
    sentence_list = [sentence for sentence in sentence_list if not '/' in sentence]
    sentence_list = [sentence for sentence in sentence_list if not '=' in sentence]
    
    # Combine list items into string.
    article = ' '.join(sentence_list)

    if len(article) < 60:
        return article

    sum = summarize(article, ratio=0.3, word_count=60)

    if len(sum) == 0: 
        return "no summary"
    else:   
        return sum

