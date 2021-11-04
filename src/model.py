import numpy as np
import torch
from torch import nn
from torch.autograd import Variable

def get_output_size(network):
    if type(network) != list:
        network = [network]
        
    output = Variable(torch.ones(1, 1, 150, 150))
    output.require_grad = False
    for conv in network:
        output = conv.forward(output)
    
    return np.prod(output.shape)


class ConvLayer(nn.Module):
    def __init__(self, in_c, out_c, kernel_size=5, max_pool_stride=2):
        super(ConvLayer, self).__init__()
        self.conv1 = nn.Conv2d(in_c, out_c, kernel_size=kernel_size)
        self.conv2 = nn.Conv2d(out_c, out_c, kernel_size=kernel_size)
        self.max_pool2d = nn.MaxPool2d(max_pool_stride)
        self.relu = nn.ReLU()

    def forward(self, x):
        x=self.conv1(x)
        x=self.relu(x)
        x=self.conv2(x)
        x=self.relu(x)
        return self.max_pool2d(x)


class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.convs = []
        self.convs.append(ConvLayer(1, 32, kernel_size=5))
        self.convs.append(ConvLayer(32, 64, kernel_size=5))
        conv_output_size = get_output_size(self.convs)
        self.fully_connected1 = nn.Linear(conv_output_size, 1024)
        self.fully_connected2 = nn.Linear(1024, 15)

    def forward(self, x):
        for conv in self.convs:
            x = conv(x)
        x = x.view(x.size(0),-1)

        x=nn.functional.relu(self.fully_connected1(x))
        return nn.functional.log_softmax(self.fully_connected2(x))