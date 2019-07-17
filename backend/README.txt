To launch sentiment analysis call evaluate("Sample string") in evaluate.py
Model is located in model2.pt
I have not tested this thoroughly, but I think it definitely needs adjustment.
So far, launch this to receive float values (range: 0 to 1) to connect the system altogether.
If the following error is observed:
    r = vocabToInt[word]  # convert words to unique integers
KeyError: 'abracadabra'
This is an indication that this word is not contained in the preset word list obtained from 1.6M tweets. I am very impressed with your vocabluary.
