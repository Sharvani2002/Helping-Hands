# Helping Hands
  Just a step away from improving 100s of lives.
  
## Description:

<b>Mission:</b> Reach a greater goal by walking ahead without looking back. 
<br>
<b>Vision:</b> Eliminate hunger and poverty.<br>
We plan to solve the following UN sustainable goals with our solution:
- Goal 1: No Poverty 
- Goal 2: Zero Hunger 

There is a huge disparity in how the resources are distributed . Some people have a lot while some have none. The people who have things in abundance often fail to realise its value and end up wasting them. We are trying to cultivate responsible consumption practices in people and also reduce hunger and poverty.

<br>
Youtube demo: https://youtu.be/tKd8x-LGLIs
<br>
  <br>
We used the below technologies to train our ML model, load the weights and make predictions of the items donated. This ensures safe and valid donations (which need to be usable) and categorizes donations for easier access. <br>
We used TinkerCAD for simulating the arduino part: The bin opens based on a passcode. The receiver needs to show the QR code which will be scanned by a bin of a particular category and opens if the QR code is valid. The QR code would first be required to be decoded by a scanning device and passed to the arduino in order to open a particular bin.


## To test the web app:
- We used a conda environment for testing our app.
- To make a conda environment from the yaml file `environment.yaml` in the root directory of our repo:
  ```
  conda env create --file environment.yaml
  ```
  or 
  ```
  conda env create -f <environment-name>.yml
  ```
- Activate the environment:
  ```
  conda activate tf
  ```
- Clone the repo, go to the helpers directory and run `python manage.py runserver`
- Go to the localhost location
- Home Page: `http://127.0.0.1:8000/`
- More details about the arduino section is in the <a href="https://github.com/Sharvani2002/helping_hands/tree/arduino">`arduino`</a> branch.

## Installations needed:
- Python version: `Python 3.8.8`
- conda version: `conda 4.8.3`
- Tensorflow, Keras, Django, h5py
- Preferably make a conda virtual env, install them in that and use it.
- If you face any issues uncomment and change`os.environ['CUDA_VISIBLE_DEVICES'] = '-1'` to `os.environ['CUDA_VISIBLE_DEVICES'] = '0'` or other value accordingly in these files:
  - `helpers/helpers/settings.py` ,  `helpers/apphelp/predict.py` and `helpers/apphelp/views.py`.
- Other installations needed: 
  - `pip install Pillow`
  - For QR code generator, you need to install this: `pip install django-qr-code`
- A list of dependencies are present in `requirements.txt` file in the root directory.

## Working of the arduino-based circuit 
- A servo motor is used to drive the lock and the push button on the left acts as the box opening button, the one on the right acts a Reed Switch (door is closed == on)
- The PASSCODE to be matched is 6512df4(for testing), the LED glows based on the comparison between entered passcode and '6512df4'.
- Red Led is the status indicator, blue is for the Alarm, and green is for the case when the passcode matches.  
- This circuit (simulated on Tinkercad) is a basic prototype of our intended model and needs further revision in terms of design. 

## Datasets used:
- Clothes/Daily necessities:
  - https://github.com/zalandoresearch/fashion-mnist
  - https://www.kaggle.com/salil007/caavo
  - https://www.kaggle.com/imneonizer/normal-vs-camouflage-clothes
  - https://www.kaggle.com/mykolarobot/share-clothes-dataset
- Garbage:
  - https://www.kaggle.com/arfathbaigs/garbageclassification-final
  - https://www.kaggle.com/mostafaabla/garbage-classification
- Food:
  - https://www.kaggle.com/kmader/food41?select=food_c101_n10099_r64x64x1.h5
  - https://www.kaggle.com/vermaavi/food11
- Money:
  - https://www.kaggle.com/husamaamer/iraqi-currency-
