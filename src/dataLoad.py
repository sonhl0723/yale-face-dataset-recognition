import os
from PIL import Image
from torch.utils.data import DataLoader, random_split
from torchvision import transforms, datasets
from torch.utils.data import Dataset

def load():
    data_path = './yalefaces'
    save_path = './preprocessing'

    if not os.path.isdir(save_path):
        os.mkdir(save_path)

        for file_name in os.listdir(data_path):
            if not 'gif' in file_name and not 'txt' in file_name and not 'DS_Store' in file_name:
                image = Image.open(data_path + '/' + file_name)
                subject_num = file_name.split('.')[0]
                img_path = save_path + '/' + subject_num + '/' + file_name + '.jpg'
                
                if not os.path.isdir(save_path + '/' + subject_num):
                    os.mkdir(save_path + '/' + subject_num)
                if not os.path.isfile(img_path):
                    image.save(img_path)
    else:
        print("Already Completed")

def preprocessing():
    trans = transforms.Compose([transforms.Resize((150,150)),
                            transforms.ToTensor(),
                            transforms.Grayscale(num_output_channels=1)
                            ])

    data = datasets.ImageFolder(root = './preprocessing', transform = trans)

    train_dataset, test_dataset  = random_split(data, [130,34])

    batch_size = 16

    yaledata = {'train_load' : DataLoader(train_dataset, batch_size = batch_size, shuffle=True),
                'test_load' : DataLoader(test_dataset, batch_size = batch_size)}

    return yaledata