import spacy
import pandas as pd
import operator

# nlp is the library of the english language
nlp = spacy.load('en_core_web_sm')


def entity(x):
    # categorizes each word that is relevant as an entity
    # x = "Federal authorities are investigating whether Deutsche Bank complied with laws meant "
    doc = nlp(x)
    orgs = {}
    # looking at each of the entities found within the text
    for ent in doc.ents:
        if ent.label_ == 'ORG':  # if the entity is labeled as an organization
            ent_name = ent.text

            if ent_name in orgs:
                orgs[ent_name] += 1
            else:
                orgs[ent_name] = 1
    sorted_orgs = sorted(orgs.items(), key=operator.itemgetter(1))
    found = sorted_orgs[-1]
    return found[0]



# maps entity name to corresponding ticker
def find_ticker(ent_name):
    xl = pd.read_excel('ticker.xlsx')  # read excel doc with entites/tickers
    names = xl['Name']  # creates array of names in 'Name' column
    tickers = xl['Ticker']  # creates array of tickers in 'Ticker' column
    i = 0  # counter
    for name in names:
        if ent_name in name:
            ticker = tickers[i]
            return ticker
        i += 1

