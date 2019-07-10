import json
from string import punctuation
from collections import Counter
import os

textList = list()
senList = list()

posFileNames = os.listdir("pos/")
negFileNames = os.listdir("neg/")
for name in posFileNames:
    with open("pos/" + name, "r") as f:
        lines = f.readlines()
        text = ''
        for line in lines:
            text = text + line + ' '
        text = ''.join([c for c in text if c not in punctuation])
        text = text.lower()
        textList.append(text)
        senList.append(1)
for name in negFileNames:
    with open("neg/" + name, "r") as f:
        lines = f.readlines()
        text = ''
        for line in lines:
            text = text + line + ' '
        text = ''.join([c for c in text if c not in punctuation])
        text = text.lower()
        textList.append(text)
        senList.append(0)
print("Finished reading file")

# add new word dict
all_text = ' '.join(textList)  # this should create 1 string holding all tweets
words = all_text.split()
count_words = Counter(words)
print(count_words)
total_words = len(words)
sorted_words = count_words.most_common(total_words)
vocabToInt = {w: i+1 for i, (w, c) in enumerate(sorted_words)}  # create a dictionary mapping the individual words
                                                                # to unique integers

# vocabToInt = vocabToInt1.copy()
# vocabToInt.update(vocabToInt2)
json.dump(vocabToInt, open("dictionaryIMDB.json", 'w'))
