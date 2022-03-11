# Recognition model using Yale Face Datset
  - [Setting](#setting)
  - [Manual](#manual)
  - [Model Architecture](#model)
    - [Original Model](#original-model)
    - [FGM Model](#model-trained-with-fgm-examples)
    - [PGD Model](#model-trained-with-pgd-examples)
  - [Algorithm](#algorithm)
  - [Experiment](#experiment)
    - [Case 1](#case-1)
    - [Case 2](#case-2)
    - [Case 3](#case-3)
  - [Reference](#reference)

## Setting
- **Dataset** : Yale Face Dataset
- **Model** : CNN
- **Environment**
  - virtualenv=20.4.2
  - Details are in **_requirements.txt_**

## Manual
- Setting
  1. git clone this repo
  2. source bin/activate
  3. pip install -r requirements.txt
- Train a model and Save as model.pt & Test accuracy
  1. python main.py --execTrain=1 --saved=1
    - if don't want to save the model, ignore --saved option
- Demo
  - python demo.py

## Model
### Original Model
<p align="center"><img src="./readme_img/model.png" width="80%" height="80%">

### Model trained with FGM Examples
### Model trained with PGD Examples

## Performance
- Epoch : 50 / Learning Rate : 0.01
- Loss
![loss_img](./readme_img/loss.png)
- Accuracy
![accuracy_img](./readme_img/accuracy.png)

## Demo
- Select random image from original 164 data and predict
- The normal image of the predicted is shown for compare
![demo_img](./readme_img/demo.png)