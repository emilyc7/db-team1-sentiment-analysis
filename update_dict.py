import json
from string import punctuation
from collections import Counter

<<<<<<< HEAD

=======
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
textList = list()
senList = list()
with open("output_data_shuffled.txt", "r") as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        if line.__contains__(","):
            sentiment, text = line.split(",", 1)
            text = ''.join([c for c in text if c not in punctuation])
            text = text.lower()
            while len(text) < 140:
                text = text + " "
            textList.append(text)
<<<<<<< HEAD
            # senList.append((ord(sentiment[1]) - 48)/5.0)
            if (ord(sentiment[1]) - 48) > 0:
                senList.append(1)
            else:
                senList.append(0)
print("Finished reading file")

# load existing word dict
dictFileName = "dictionaryBinary.json"
# vocabToInt1 = json.load(open(dictFileName, 'r'))  # load the dictionary
=======
            senList.append((ord(sentiment[1]) - 48)/5.0)
print("Finished reading file")

# load existing word dict
dictFileName = "dictionary.json"
vocabToInt1 = json.load(open(dictFileName, 'r'))  # load the dictionary
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3

# add new word dict
all_text = ' '.join(textList)  # this should create 1 string holding all tweets
words = all_text.split()
count_words = Counter(words)
print(count_words)
total_words = len(words)
sorted_words = count_words.most_common(total_words)
<<<<<<< HEAD
vocabToInt = {w: i+1 for i, (w, c) in enumerate(sorted_words)}  # create a dictionary mapping the individual words
                                                                # to unique integers

# vocabToInt = vocabToInt1.copy()
# vocabToInt.update(vocabToInt2)
json.dump(vocabToInt, open("dictionaryBinary.json", 'w'))
=======
vocabToInt2 = {w: i+1 for i, (w, c) in enumerate(sorted_words)}  # create a dictionary mapping the individual words
                                                                # to unique integers

vocabToInt = vocabToInt1.copy()
vocabToInt.update(vocabToInt2)
json.dump(vocabToInt, open("dictionary1.json", 'w'))
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
