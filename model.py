import torch
import torchtext
from tokenizer import get_tokenizer
path = "dataset path"

#load first 40,000 lines to train,use last 10 to test


#data needs to be tokenized and have punction marks and things removed
def load_data():
    tokenizer = get_tokenizer("basic english")
    tokens = tokenizer("this is a sentence")
    print(tokens)

def train_data():
    pass

class model():
    def __init__(self):
        super().__init__()

    def foward(self):
        pass

def main():
    load_data()

main()
