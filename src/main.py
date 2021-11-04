from model import Network, ConvLayer
import test
import train
import dataLoad
import demo
import argparse
import torch
from PIL import Image
from torch import optim


parser = argparse.ArgumentParser(description="Recognize using CNN")

parser.add_argument("--execTrain", type=int, default=0,
                help="Decide whether to train with trainset")
parser.add_argument("--lr", type=float, default=0.001, metavar="L",
                help="Learning Rate")
parser.add_argument("--saved", type=int, default=0, metavar="L",
                help="Learning Rate")

args = parser.parse_args() 

def main(args):
    dataLoad.load()
    pre_data=dataLoad.preprocessing()
    
    model=Network()

    if args.execTrain:
        optimizer=optim.Adam(model.parameters(), args.lr)
        train.main(model, optimizer, pre_data['train_load'], args.saved)
    else: model=torch.load('./model.pt')

    test.main(model, pre_data['test_load'])

if __name__ == '__main__':
    main(args)