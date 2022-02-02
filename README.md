# NoteIt

A simple, personal notes app written in Python.
Meant to be a CRUD demonstration. Uses SQLite.
You can [try the public demo.](https://wkinzu.pythonanywhere.com/)

## Roadmap

- [ ] Notebooks (collections)
- [ ] Created, Last Updated
- [ ] Markdown
- [ ] Multiple users
- [ ] Tags, colors
- [ ] UI improvments

## Run locally

1. Clone the repo, create a virtual environment and install the dependencies
     ```
     git clone https://github.com/nityy/NoteIt.git
     cd NoteIt
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```
2. Generate a random Django secret key and write it to `.env`
     ```
     echo "SECRET_KEY='$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')'" > .env
     ```
3. Apply Migrations (create database)
     ```
     python manage.py migrate
     ```
4. Run the server
     ```
     python manage.py runserver
     ```
     Open `127.0.0.1:8000` in your browser

---
The favicon was generated using Twemoji licensed under CC-BY 4.0
