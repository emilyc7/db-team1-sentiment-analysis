import spacy

# nlp is the library of the english language
nlp = spacy.load('en')


def entity(x):
    # categorizes each word that is relevant as an entity
    # x = "Federal authorities are investigating whether Deutsche Bank complied with laws meant "
    doc = nlp(x)

    # looking at each of the entities found within the text
    for ent in doc.ents:
        if ent.label_ == 'ORG':  # if the entity is labeled as an organization
            print(ent.text)  # print the text of the entity (what was in the text i.e. Deutsche Bank or DB)
    return
