# Helping Hands
  Just a step away from improving 100s of lives...
  
## To test the web app:
- Clone the repo, go to the helpers directory and run `python manage.py runserver`
- Go to the localhost location
- Leaderboard: `http://127.0.0.1:8000/leaderboard`
- Donate Page: `http://127.0.0.1:8000/donate`
- Home Page: `http://127.0.0.1:8000/`
- Arduino part is in the <a href="https://github.com/Sharvani2002/helping_hands/tree/arduino">`arduino`</a> branch.

## Installations needed:
- Tensorflow
       `pip install tensorflow`
- Keras
- Django
       `pip install django`
- Preferably make a conda virtual env, install them in that and use it.
- If you have a separate GPU (not the one integrated with CPU) and want to enable it, comment `os.environ['CUDA_VISIBLE_DEVICES'] = '-1'` in these files:
  - `helpers/helpers/settings.py` ,  `helpers/apphelp/predict.py` and `helpers/apphelp/views.py`.
  - If that doesn't work, change `os.environ['CUDA_VISIBLE_DEVICES'] = '-1'` to `os.environ['CUDA_VISIBLE_DEVICES'] = '0'` in the above 3 files. 
- Other installations needed: 
  - `pip install Pillow`
  - For QR code generator, you need to install this: `pip install django-qr-code`

## Other details (our reference): 
- the donated images are stored as `<path to the app>/static/donations/user_id_1_1.jpg`
- More specifically, the last part is `user_id_<id>_<donation number>.jpg`
- check the images folder for the web app pages and demo

## Working of the arduino-based circuit 
- A servo motor is used to drive the lock and the push button on the left acts as the box opening button, the one on the right acts a Reed Switch (door is closed == on)
- The PASSCODE to be matched is 6512df4(for testing), the LED glows based on the comparison between entered passcode and '6512df4'.
- Red Led is the status indicator, blue is for the Alarm, and green is for the case when the passcode matches.  
- This circuit (simulated on Tinkercad) is a basic prototype of our intended model and needs further revision in terms of design. 

## Datasets
Clothes/Daily necessities:
- https://github.com/zalandoresearch/fashion-mnist
- https://www.kaggle.com/salil007/caavo
- https://www.kaggle.com/imneonizer/normal-vs-camouflage-clothes
- https://www.kaggle.com/mykolarobot/share-clothes-dataset

Garbage:
- https://www.kaggle.com/arfathbaigs/garbageclassification-final
- https://www.kaggle.com/mostafaabla/garbage-classification

Food:
- https://www.kaggle.com/kmader/food41?select=food_c101_n10099_r64x64x1.h5
- https://www.kaggle.com/vermaavi/food11

Money:
- https://www.kaggle.com/husamaamer/iraqi-currency-
