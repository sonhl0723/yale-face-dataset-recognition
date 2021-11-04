import torch
from torch.autograd import Variable

def main(model, loader):
    model.eval()
    validation_loss = 0
    correct = 0

    for image, label in loader:
        image, label = Variable(image, volatile=True), Variable(label)

        output = model(image)
        validation_loss += torch.nn.functional.nll_loss(output, label, size_average=False)
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(label.data.view_as(pred)).cpu().sum()

    validation_loss /= len(loader.dataset)
    print('\n' + ' set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'
        .format(validation_loss, correct, len(loader.dataset),
                100. * correct / len(loader.dataset)))

    return 100 * correct / len(loader.dataset)