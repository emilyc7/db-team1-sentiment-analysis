from create_NN import create_NN
import torch
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import json
import nltk
from nltk.corpus import stopwords
from string import punctuation


def evaluate_NN(all_text, dictFileName="/Users/emilycroxall/Documents/sentiment-analysis/backend/dictionaryIMDB.json", seqLen=500):
    train_on_gpu = torch.cuda.is_available()
    device = torch.device('cuda' if train_on_gpu else 'cpu')
    vocabToInt = json.load(open(dictFileName, 'r'))  # load the dictionary
    all_text = all_text.lower()
    all_text = ''.join([c for c in all_text if c not in punctuation])
    words = all_text.split()  # make an array of words
    stopwordList = set(stopwords.words('english'))
    textListNum = list()  # to become list of lists holding tweets and words
    r1 = list()
    for word in words:  # iterate through text tweet by tweet
        if word in vocabToInt and word not in stopwordList:
            r = vocabToInt[word]  # convert words to unique integers
            r1.append(r)
    textListNum.append(r1)

    while len(textListNum[0]) < seqLen:  # force to uniform length
        textListNum[0].append(0)
    if len(textListNum[0]) > seqLen:
        textListNum[0] = textListNum[0][:seqLen]
    inputs = torch.tensor(np.array(textListNum), device=device)
    # load the model
    device = torch.device(device)
    net = create_NN(len(vocabToInt)+1)
    if train_on_gpu:
        net.load_state_dict(torch.load("/Users/emilycroxall/Documents/sentiment-analysis/backend/model5.pt"))
    else:
        net.load_state_dict(torch.load("/Users/emilycroxall/Documents/sentiment-analysis/backend/model5.pt", map_location={'cuda:0': 'cpu'}))
    # print(net)
    if train_on_gpu:
        net.cuda(device)
    # run 1 forward test loop iteration
    # output = net.test_model(1, inputs)
    net.eval()
    h = net.init_hidden(1, train_on_gpu)
    h = tuple([each.data for each in h])
    inputs = inputs.to(torch.int64)
    output = net(inputs, h)
    output = output[0]
    if train_on_gpu:
        output = output.cpu().detach().numpy()[0]
    else:
        output = output.detach().numpy()[0]
    print("p = " + str(output))
    return output


# evaluate_NN("This is amazing!")
# evaluate_NN("The stock outlook for this month is very negative")
# evaluate_NN("This is terrible")