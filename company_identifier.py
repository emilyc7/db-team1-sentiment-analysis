import spacy

# nlp is the library of the english language
nlp = spacy.load('en')

# categorizes each word that is relevant as an entity
doc = nlp(u"Federal authorities are investigating whether Deutsche Bank complied with laws meant "
          u"to stop money laundering and other crimes, the latest government examination of potential "
          u"misconduct at one of the world’s largest and most troubled banks, according to seven people "
          u"familiar with the inquiry. The investigation includes a review of Deutsche Bank’s handling "
          u"of so-called suspicious activity reports that its employees prepared about possibly problematic "
          u"transactions, including some linked to President Trump’s son-in-law and senior adviser, "
          u"Jared Kushner, according to people close to the bank and others familiar with the matter. The criminal "
          u"investigation into Deutsche Bank is one element of several separate but overlapping government "
          u"examinations into how illicit funds flow through the American financial system, said five of the people, "
          u"who were not authorized to speak publicly about the inquiries. Several other banks are also being "
          u"investigated. The F.B.I. recently contacted the lawyer for a Deutsche Bank whistle-blower, "
          u"Tammy McFadden, who publicly criticized the company’s anti-money-laundering systems, according to "
          u"the lawyer, Brian McCafferty.")

# looking at each of the entities found within the text
for ent in doc.ents:
    if ent.label_ == 'ORG':  # if the entity is labeled as an organization
        print(ent.text)  # print the text of the entity (what was in the text i.e. Deutsche Bank or DB)
