import numpy as np
from string import punctuation
from collections import Counter
from create_NN import create_NN
import json
import torch
from torch.utils.data import DataLoader, TensorDataset

train_on_gpu = True

# ### THIS LINE DEFINES A GPU, OTHERWISE CPU IS DEFAULT, UNCOMMENT IF YOU HAVE A GPU ###

train_on_gpu = torch.cuda.is_available()
# train_on_gpu = False
device = torch.device('cuda:0' if train_on_gpu else 'cpu')

print(device)

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
            senList.append((ord(sentiment[1]) - 48)/5.0)
            # if i == 200000:
            #     break
print("Finished reading file")

# load existing word dict
dictFileName = "dictionary1.json"
vocabToInt = json.load(open(dictFileName, 'r'))  # load the dictionary
print("Finished loading dictionary")
# add new word dict
# all_text = ' '.join(textList)  # this should create 1 string holding all tweets
# words = all_text.split()
# count_words = Counter(words)
# print(count_words)
# total_words = len(words)
# sorted_words = count_words.most_common(total_words)
# vocabToInt2 = {w: i+1 for i, (w, c) in enumerate(sorted_words)}  # create a dictionary mapping the individual words
#                                                                 # to unique integers
#
# vocabToInt = vocabToInt1.copy()
# vocabToInt.update(vocabToInt2)

textListNum = list()  # to become list of lists holding tweets and words
seqLen = 0
for text in textList:  # iterate through text tweet by tweet
    r = [vocabToInt[w] for w in text.split()]  # convert words to unique integers
    if len(r) > seqLen:  # set seqLen to be the max length of a tweet (in words)
        seqLen = len(r)
    textListNum.append(r)
print("seqLen = ")
print(seqLen)
inputs = np.zeros((len(textListNum), seqLen), dtype=int)  # 2D array formatting to suit NN batch input
i = 0
for nums in textListNum:
    while len(nums) < seqLen:
        nums.append(0)  # pad tweets with less words with zeros to match seqLen
    inputs[i, :] = np.array(nums)
    i = i+1

outputs = np.array(senList)
# create new model
# net = create_NN(len(vocabToInt)+1, device)  # +1 for the 0 padding not yet in dictionary
# load existing model
net = create_NN(len(vocabToInt) + 1, device)
# net.load_state_dict(torch.load("model.pt"))
print("Created NN")
if train_on_gpu:
    net = net.cuda(device)  # ###  CONVERSION_TO_GPU_FORMAT
    print("Transferred to GPU")
print(next(net.parameters()).is_cuda)
print("my net")
print(net)  # ### IF GPU FORMAT, SHOULD STATE SO AT THE END OF THE PRINT STATEMENT

length = len(inputs)
split1 = 0.8
split2 = 0.81
# train_x = inputs[400000:int(split1*length)]
# train_y = outputs[400000:int(split1*length)]

train_x = inputs[300000:int(split1*length)]
train_y = outputs[300000:int(split1*length)]
valid_x = inputs[int(split1*length):int(split2*length)]
print(len(valid_x))

valid_y = outputs[int(split1*length):int(split2*length)]
# test_x = inputs[int(split2*length):]
# test_y = outputs[int(split2*length):]

# create Tensor datasets
train_data = TensorDataset(torch.from_numpy(train_x), torch.from_numpy(train_y))
valid_data = TensorDataset(torch.from_numpy(valid_x), torch.from_numpy(valid_y))
# test_data = TensorDataset(torch.from_numpy(test_x), torch.from_numpy(test_y))

# dataloaders
batch_size = 50
train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size, drop_last=True)
valid_loader = DataLoader(valid_data, shuffle=True, batch_size=batch_size, drop_last=True)
# test_loader = DataLoader(test_data, shuffle=True, batch_size=batch_size)

hidden = net.init_hidden(batch_size)
net.train_model(batch_size, train_loader, valid_loader)
# net.test_model(batch_size, test_loader)
print(net)

json.dump(vocabToInt, open("dictionary.json", 'w'))
torch.save(net.state_dict(), "model2.pt")
