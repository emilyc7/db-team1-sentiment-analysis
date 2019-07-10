# credit to https://towardsdatascience.com/sentiment-analysis-using-lstm-step-by-step-50d074f09948

import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

class SentimentLSTM(nn.Module):
    """
    The RNN model that will be used to perform Sentiment analysis.
    vocab size = 140
    output size = 1
    embedding dim = 256
    hidden_dim = 100
    n_layers = 5
    """
    train_on_gpu = True

    def __init__(self, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, device=None, drop_prob=0.5):
        """
        Initialize the model by setting up the layers.
        """
        super().__init__()

        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim

        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers,
                            dropout=drop_prob, batch_first=True)

        # dropout layer
        self.dropout = nn.Dropout(0.3)

        # linear and sigmoid layers
        self.fc = nn.Linear(hidden_dim, output_size)
        # self.tanh = nn.Tanh()
        self.sig = nn.Sigmoid()
        self.device = device

    def forward(self, x, hidden):
        """
        Perform a forward pass of our model on some input and hidden state.
        """
        batch_size = x.size(0)

        # embeddings and lstm_out
        embeds = self.embedding(x)
        lstm_out, hidden = self.lstm(embeds, hidden)

        # stack up lstm outputs
        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)

        # dropout and fully-connected layer
        out = self.dropout(lstm_out)
        out = self.fc(out)
        # sigmoid function
        sig_out = self.sig(out)

        # reshape to be batch_size first
        sig_out = sig_out.view(batch_size, -1)
        sig_out = sig_out[:, -1]  # get last batch of labels

        # return last sigmoid output and hidden state
        return sig_out, hidden

    def init_hidden(self, batch_size, train_on_gpu=True):
        ''' Initializes hidden state '''
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data
        # ### CONVERSION TO CUDA
        if train_on_gpu:
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(self.device),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(self.device))
        else:
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())

        return hidden

    def train_model(self, batch_size, train_loader, valid_loader, train_on_gpu=True):
        # loss and optimization functions
        lr = 0.005
        VALLOSSES = list()

        # criterion = nn.KLDivLoss()
        # criterion = nn.MSELoss()
        # criterion = nn.CrossEntropyLoss()
        criterion = nn.BCELoss()
        criterion = criterion.cuda()
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        # training params
        epochs = 2  # 3-4 is approx where I noticed the validation loss stop decreasing

        print_every = 10
        clip = 5  # gradient clipping

        # move model to GPU, if available
        if train_on_gpu:
            self.cuda(self.device)

        self.train()
        # initialize hidden state
        h = self.init_hidden(batch_size)
        # train for some number of epochs
        for e in range(epochs):
            counter = 0
            # batch loop
            for inputs, labels in train_loader:
                if counter % print_every == 0:
                    print(counter)
                counter += 1
                # print("Model inputs")
                if train_on_gpu:
                    inputs, labels = inputs.cuda(self.device), labels.cuda(self.device)  # ### CONVERSION TO GPU FORMAT
                # print(inputs)
                # Creating new variables for the hidden state, otherwise
                # we'd backprop through the entire training history
                h = tuple([each.data for each in h])

                # zero accumulated gradients
                self.zero_grad()

                # get the output from the model
                inputs = inputs.type(torch.LongTensor)
                inputs = inputs.cuda(self.device)
                labels = labels.cuda(self.device)

                output, h = self(inputs, h)  # net()
                # calculate the loss and perform backprop
                # print(output.squeeze())
                loss = criterion(output.squeeze(), labels.float())
                loss.backward()
                # `clip_grad_norm` helps prevent the exploding gradient problem in RNNs / LSTMs.
                nn.utils.clip_grad_norm_(self.parameters(), clip)
                optimizer.step()

                # loss stats
                if counter % print_every == 0:
                    # Get validation loss
                    val_h = self.init_hidden(batch_size)
                    val_losses = []
                    self.eval()
                    i = 0
                    for inputs, labels in valid_loader:
                        # Creating new variables for the hidden state, otherwise
                        # we'd backprop through the entire training history
                        val_h = tuple([each.data for each in val_h])

                        if train_on_gpu:
                            inputs, labels = inputs.cuda(self.device), labels.cuda(self.device)  # ### CONVERSION TO GPU FORMAT
                        inputs = inputs.type(torch.LongTensor)
                        inputs = inputs.cuda(self.device)
                        labels = labels.cuda(self.device)
                        output, val_h = self(inputs, val_h)
                        # print(inputs)
                        # print(output)
                        val_loss = criterion(output.squeeze(), labels.float())
                        val_losses.append(val_loss.item())
                        i = i+1
                    self.train()
                    print("Epoch: {}/{}...".format(e + 1, epochs),
                          "Step: {}...".format(counter),
                          "Loss: {:.6f}...".format(loss.item()),
                          "Val Loss: {:.6f}".format(np.mean(val_losses)))
                    VALLOSSES.append(np.mean(val_losses))
        plt.plot(VALLOSSES)
        plt.show()
        return

    def test_model(self, batch_size, test_loader, train_on_gpu=True):
        test_losses = []  # track loss
        num_correct = 0
        # criterion = nn.KLDivLoss()
        criterion = nn.BCELoss()
        # init hidden state
        h = self.init_hidden(batch_size)

        self.eval()
        # iterate over test data
        for inputs, labels in test_loader:

            # Creating new variables for the hidden state, otherwise
            # we'd backprop through the entire training history
            h = tuple([each.data for each in h])

            if train_on_gpu:
                inputs, labels = inputs.cuda(device=self.device), labels.cuda(device=self.device)  # ### CONVERSION TO GPU FORMAT

            # get predicted outputs
            inputs = inputs.type(torch.LongTensor)
            inputs = inputs.cuda(self.device)
            labels = labels.cuda(self.device)
            output, h = self(inputs, h)


            # calculate loss
            test_loss = criterion(output.squeeze(), labels.float())
            test_losses.append(test_loss.item())

            # convert output probabilities to predicted class (0 or 1)
            pred = torch.round(output.squeeze())  # rounds to the nearest integer

            # compare predictions to true label
            correct_tensor = pred.eq(labels.float().view_as(pred))
            if train_on_gpu:
                correct = np.squeeze(correct_tensor.cpu().numpy())
            else:
                correct = np.squeeze(correct_tensor.numpy())
            # correct = np.squeeze(correct_tensor.numpy()) if not train_on_gpu else np.squeeze(correct_tensor.cpu().numpy())
            num_correct += np.sum(correct)

        # -- stats! -- ##
        # avg test loss
        print("Test loss: {:.3f}".format(np.mean(test_losses)))

        # accuracy over all test data
        test_acc = num_correct / len(test_loader.dataset)
        print("Test accuracy: {:.3f}".format(test_acc))
        return output.cpu().detach().numpy()[0]
