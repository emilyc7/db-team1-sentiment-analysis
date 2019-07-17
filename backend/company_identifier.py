import spacy
import pandas as pd

# nlp is the library of the english language
nlp = spacy.load('en_core_web_sm')


def entity(x):
    # categorizes each word that is relevant as an entity
    # x = "Federal authorities are investigating whether Deutsche Bank complied with laws meant "
    doc = nlp(x)

    # looking at each of the entities found within the text
    for ent in doc.ents:
        if ent.label_ == 'ORG' and ent.text != 'Financial Times':  # if the entity is labeled as an organization
            if ent.text == "Deutsche Bank DB" or ent.text == "DB Deutsche Bank" or ent.text == "DB":
                ent_name = "Deutsche Bank"
                return ent_name
            ent_name = ent.text
            return ent_name


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

