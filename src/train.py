import numpy as np
from torch.autograd import Variable
import torch
from model import Network
from torch.nn.functional import nll_loss

def main(model, optimizer, dataset, isSave):
    epochs=10
    model.train()
    for i in range(epochs):
        loss_data=[]
        for images, labels in dataset:
            images, labels = Variable(images), Variable(labels)

            optimizer.zero_grad()

            output = model(images)

            loss = nll_loss(output, labels)
            loss.backward()
            optimizer.step()
            loss_data.append(loss.data)

        print('Train Epoch: {} \tLoss: {:.6f}'.format(i, np.mean(loss_data)))

    if isSave:
        torch.save(model, './model.pt')