import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

def summary(url):
    page = requests.get(url).text

    soup = BeautifulSoup(page)
    
    p_tags = soup.find_all('p') 
    p_tags_text = [tag.get_text().strip() for tag in p_tags]

    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    # Combine list items into string.
    article = ' '.join(sentence_list)

    summary = summarize(article, ratio=0.3)

    print(summary)

   