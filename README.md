# google_solutions_challenge

## To test the web app:
- Clone the repo, go to the helpers directory and run `python manage.py runserver`
- Go to the localhost location
- Leaderboard: `http://127.0.0.1:8000/leaderboard`
- Donate Page: `http://127.0.0.1:8000/donate`
- Home Page: `http://127.0.0.1:8000/`

## Installations needed:
- Tensorflow, Keras, Django
- Preferably make a conda virtual env, install them in that and use it.
- If you have a separate GPU (not the one integrated with CPU) and want to enable it, comment `os.environ['CUDA_VISIBLE_DEVICES'] = '-1'` in these files:
  - `helpers/helpers/settings.py` ,  `helpers/apphelp/predict.py` and `helpers/apphelp/views.py`.
  - If that doesn't work, change `os.environ['CUDA_VISIBLE_DEVICES'] = '-1'` to `os.environ['CUDA_VISIBLE_DEVICES'] = '0'` in the above 3 files. 
- Other installations needed: 
  - `pip install Pillow`
  - For QR code generator, you need to install this: `pip install django-qr-code`

## Other details: 
- the donated images are stored as `<path to the app>/static/donations/user_id_1_1.jpg`
- More specifically, the last part is `user_id_<id>_<donation number>.jpg`
- check the images folder for the web app pages and demo
