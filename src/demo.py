import random
from model import Network, ConvLayer
import torch
import os
from torch.autograd import Variable
import matplotlib.pyplot as plt
from torchvision import transforms, datasets
import numpy as np
from PIL import Image

def main():
    model=Network()
    model=torch.load('./model.pt')
    model.eval()

    trans = transforms.Compose([transforms.Resize((150,150)),
                            transforms.ToTensor(),
                            transforms.Grayscale(num_output_channels=1)
                            ])
    dataset = datasets.ImageFolder(root = './preprocessing/', transform = trans)
    
    demo_data = dataset[random.randint(0, len(os.listdir('./preprocessing'))-1)]
    image = Variable(demo_data[0])
    image = image.unsqueeze(0)

    output = model(image)
    result = torch.max(output, 1)

    trans_image = transforms.ToPILImage()

    label_index = int(str(int(result.indices[0])))+1

    print("---------------------------------------------")
    print("Origin subject's normal image")
    if(label_index<10):
        image_pil = Image.open('./preprocessing/subject0' + str(label_index) + '/subject0' + str(label_index) + '.normal.jpg')
    else:
        image_pil = Image.open('./preprocessing/subject' + str(label_index) + '/subject' + str(label_index) + '.normal.jpg')
    image = np.array(image_pil)

    fig = plt.figure()
    rows = 1
    cols = 2
    ax1 = fig.add_subplot(rows, cols, 1)
    ax1.imshow(trans_image(demo_data[0]), plt.get_cmap("gray"))
    ax1.set_title("Predict subject is subject: "+str(label_index))
    ax1.axis("off")
    
    ax2 = fig.add_subplot(rows, cols, 2)
    ax2.imshow(image, cmap = plt.get_cmap("gray"))
    ax2.set_title("Origin subject's normal image")
    ax2.axis("off")
    
    plt.show()

if __name__ == '__main__':
    main()