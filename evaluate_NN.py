from create_NN import create_NN
import torch
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import nltk
import json


def evaluate_NN(all_text, device, dictFileName="dictionary1.json", seqLen=40):
    train_on_gpu = torch.cuda.is_available()
    device = torch.device('cuda:0' if train_on_gpu else 'cpu')

    vocabToInt = json.load(open(dictFileName, 'r'))  # load the dictionary
    all_text = all_text.lower()
    words = all_text.split()  # make an array of words
    textListNum = list()  # to become list of lists holding tweets and words
    r1 = list()
    for word in words:  # iterate through text tweet by tweet
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
    net.load_state_dict(torch.load("model2.pt"))
    print(net)
    net.cuda(device)
    # run 1 forward test loop iteration
    # output = net.test_model(1, inputs)
    net.eval()
    h = net.init_hidden(1)
    h = tuple([each.data for each in h])
    output = net(inputs, h)
    print(output)
    output = output[0]
    output = output.cpu().detach().numpy()[0]
    print("p = " + str(output))
    return

