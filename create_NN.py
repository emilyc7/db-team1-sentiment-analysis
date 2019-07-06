from NN_model import SentimentLSTM


def create_NN(inputLen, device=None):
    output_size = 1
    embedding_dim = 500
    hidden_dim = 256
    n_layers = 2
    device = device
    return SentimentLSTM(inputLen, output_size, embedding_dim, hidden_dim, n_layers, device=device)
