import argparse
from transformers import BertModel, BertTokenizer
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description="Fine-tune BERT model for sentiment classification")
parser.add_argument("--freeze", required=True, help="Want to freeze the parameters of pretrained BERT model?",
                    type = str2bool, default = "True")
parser.add_argument("--epochs", required=True, help="the number of training epochs", type=int)

args = parser.parse_args()
freeze = args.freeze
epochs = args.epochs


class Movie(Dataset):
    def __init__(self, filename):

        self.df = pd.read_csv(filename)
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.maxlen = self.get_max_len()

    def get_max_len(self):

        sentences = self.df['review']
        max_len = len(self.tokenizer.tokenize(sentences[0]))

        for sentence in sentences[1:]:
            new_len = len(self.tokenizer.tokenize(sentence))
            if new_len > max_len:
                max_len = new_len

        return max_len + 3

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):

        T = 512  # bert maxlen

        review = self.df['review'][index]
        sentiment = torch.Tensor([self.df['sentiment'][index]])

        tokens = self.tokenizer.tokenize(review)
        tokens = ['[CLS]'] + tokens + ['[SEP]']

        if len(tokens) < T:
            tokens = tokens + ['[PAD]' for _ in range(T - len(tokens))]
        else:
            tokens = tokens[:T]

        token_ids = self.tokenizer.convert_tokens_to_ids(tokens)
        token_ids_tensor = torch.LongTensor(token_ids).view(-1,)

        attn_mask = (token_ids_tensor != 0).long()

        return token_ids_tensor, attn_mask, sentiment

data = Movie('../data/movie.csv')
data_loader = DataLoader(data, batch_size=32, shuffle=True)

class SentimentClassifier(torch.nn.Module):

    def __init__(self, freeze=freeze):
        super(SentimentClassifier, self).__init__()
        self.bert_layer = BertModel.from_pretrained('bert-base-uncased')

        if freeze:
            for p in self.bert_layer.parameters():
                p.requires_grad = True

        self.cls_layer = torch.nn.Linear(768, 1)

    def forward(self, seq, attn_masks):

        cont_reps, _ = self.bert_layer(seq, attention_mask=attn_masks)
        cls_rep = cont_reps[:, 0]

        logits = self.cls_layer(cls_rep)

        return logits

device = "cuda" if torch.cuda.is_available() else "cpu"

net = SentimentClassifier(freeze=freeze).to(device)
criterion = torch.nn.BCEWithLogitsLoss().to(device)
optimizer = torch.optim.Adam(net.parameters(), lr=2e-5)

def train():

    net.train()
    losses = []

    for epoch in range(epochs):

        for it, (seq, attn_masks, labels) in enumerate(data_loader):
            optimizer.zero_grad()
            seq, attn_masks, labels = seq.to(device), attn_masks.to(device), labels.to(device)

            logits = net(seq, attn_masks)
            loss = criterion(logits.view_as(labels), labels.float())
            losses.append(loss.item())

            loss.backward()
            optimizer.step()

            if it % 20 == 0:

                pred = logits > 0.5
                acc = (pred.squeeze().long() == labels.squeeze().long()).sum().item() / logits.shape[0]
                print(f"Epoch: {epoch+1}, Iteration: {it+1}, Loss: {loss.item()}, Accuracy: {acc}")


    return losses


if __name__ == "__main__":
    losses = train()
    plt.plot(range(1, len(losses)+1), losses)
    plt.title("Loss")
    torch.save(net.state_dict(), "./BERT_finetune.pth")







