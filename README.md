# Yale-FaceRecognition
- dataset : Yale Face Dataset
- Model : CNN
- environment : virtualenv=20.4.2 / MacOS(Catalina 10.15.7)

## How to Use
- Setting
  1. git clone this repo
  2. source bin/activate
  3. pip install -r requirements.txt
- Train a model and Save as model.pt & Test accuracy
  1. python main.py --execTrain=1 --saved=1
    - if don't want to save the model, ignore --saved option
- Demo
  - python demo.py

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