from create_NN import create_NN
import torch
from torch.utils.data import DataLoader, TensorDataset
<<<<<<< HEAD
=======
from string import punctuation
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
import numpy as np
import nltk
import json

<<<<<<< HEAD

def evaluate_NN(all_text, dictFileName="dictionaryIMDB.json", seqLen=40):
    train_on_gpu = torch.cuda.is_available()
    device = torch.device('cuda:0' if train_on_gpu else 'cpu')
    vocabToInt = json.load(open(dictFileName, 'r'))  # load the dictionary
    all_text = all_text.lower()
=======
def evaluate_NN(all_text, dictFileName="dictionaryIMDB.json", seqLen=40):
    train_on_gpu = torch.cuda.is_available()
    device = torch.device('cuda:0' if train_on_gpu else 'cpu')

    vocabToInt = json.load(open(dictFileName, 'r'))  # load the dictionary
    all_text = all_text.lower()
    all_text = ''.join(c for c in all_text if c not in punctuation)
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
    words = all_text.split()  # make an array of words
    textListNum = list()  # to become list of lists holding tweets and words
    r1 = list()
    for word in words:  # iterate through text tweet by tweet
<<<<<<< HEAD
        r = vocabToInt[word]  # convert words to unique integers
        r1.append(r)
=======
        if word in vocabToInt:
            r = vocabToInt[word]  # convert words to unique integers
            r1.append(r)
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
    textListNum.append(r1)

    while len(textListNum[0]) < seqLen:  # force to uniform length
        # textListNum[0].append(0)
        textListNum[0].append(np.random.randint(0, len(vocabToInt)))
    if len(textListNum[0]) > seqLen:
        textListNum[0] = textListNum[0][:seqLen]
<<<<<<< HEAD
=======
        print(textListNum)
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
    inputs = torch.tensor(np.array(textListNum), device=device)
    # load the model
    device = torch.device(device)
    net = create_NN(len(vocabToInt)+1)
    if train_on_gpu:
        net.load_state_dict(torch.load("model2.pt"))
    else:
        net.load_state_dict(torch.load("model2.pt", map_location={'cuda:0': 'cpu'}))
    print(net)
    if train_on_gpu:
        net.cuda(device)
    # run 1 forward test loop iteration
    # output = net.test_model(1, inputs)
    net.eval()
    h = net.init_hidden(1, train_on_gpu)
<<<<<<< HEAD
    h = tuple([each.data for each in h])
    output = net(inputs, h)
    print(output)
=======

    h = tuple([each.data for each in h])
    output = net(inputs, h)
    # print(output)
>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3
    output = output[0]
    if train_on_gpu:
        output = output.cpu().detach().numpy()[0]
    else:
        output = output.detach().numpy()[0]
    print("p = " + str(output))
    return output


<<<<<<< HEAD
evaluate_NN("amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing")
=======
# evaluate_NN("amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing amazing")

>>>>>>> 8cbc7e1e0fd702f31dabc0d5bbdc995af9b7ead3

