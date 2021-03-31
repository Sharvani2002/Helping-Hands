# google_solutions_challenge

## To test the web app:
- Clone the repo, go to the helpers directory and run `python manage.py runserver`
- Go to the localhost location
- Leaderboard: `http://127.0.0.1:8000/leaderboard`
- Donate Page: `http://127.0.0.1:8000/donate`
- Home Page: `http://127.0.0.1:8000/`
- For QR code generator, you need to install this: `pip install django-qr-code`
- the donated images are stored as `<path to the app>/static/donations/user_id_1_1.jpg`
- More specifically, the last part is `user_id_<id>_<donation number>.jpg`
- check the images folder for the web app pages and demo
