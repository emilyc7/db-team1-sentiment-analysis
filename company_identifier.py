import spacy
import pandas as pd

# nlp is the library of the english language
nlp = spacy.load('en')


def entity(x):
    # categorizes each word that is relevant as an entity
    # x = "Federal authorities are investigating whether Deutsche Bank complied with laws meant "
    doc = nlp(x)
    ent_name = ""

    # looking at each of the entities found within the text
    for ent in doc.ents:
        if ent.label_ == 'ORG' and ent.text != 'Financial Times':  # if the entity is labeled as an organization
            if ent.text == "Deutsche Bank DB" or ent.text == "DB Deutsche Bank" or ent.text == "DB":
                ent_name = "Deutsche Bank"
                print("Deutsche Bank")
                break
            ent_name = ent.text
            print(ent.text)  # print the text of the entity (what was in the text i.e. Deutsche Bank or DB)
            break
    find_ticker(ent_name)
    return


def find_ticker(ent_name):
    xl = pd.read_excel('ticker.xlsx')
    names = xl['Name']
    tickers = xl['Ticker']
    i = 0
    for name in names:
        if ent_name in name:
            ticker = tickers[i]
            print(ticker)
            return
        i += 1
